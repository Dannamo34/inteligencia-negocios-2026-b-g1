import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(2026)

CARPETA = Path(__file__).parent

def guardar_csv(nombre, columnas, registros):
    ruta = CARPETA / nombre

    with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(registros)

    print(f"Archivo creado: {nombre} ({len(registros)} registros)")


# --------------------------------------------------
# 1. DIMENSION DE FECHAS
# --------------------------------------------------

fechas = []
fecha_actual = date(2025, 1, 1)
fecha_final = date(2025, 12, 31)

while fecha_actual <= fecha_final:
    fechas.append({
        "id_fecha": int(fecha_actual.strftime("%Y%m%d")),
        "fecha": fecha_actual.isoformat(),
        "dia": fecha_actual.day,
        "mes": fecha_actual.month,
        "nombre_mes": fecha_actual.strftime("%B"),
        "trimestre": f"T{((fecha_actual.month - 1) // 3) + 1}",
        "anio": fecha_actual.year
    })
    fecha_actual += timedelta(days=1)

guardar_csv(
    "dim_fecha.csv",
    ["id_fecha", "fecha", "dia", "mes", "nombre_mes",
     "trimestre", "anio"],
    fechas
)


# --------------------------------------------------
# 2. DIMENSION DE PRODUCTOS
# --------------------------------------------------

categorias = ["Aretes", "Collares", "Pulseras", "Anillos"]

materiales = [
    "Acero inoxidable",
    "Mostacilla",
    "Miyuki",
    "Plata",
    "Bisuteria"
]

productos = []

for i in range(1, 31):
    categoria = random.choice(categorias)
    precio = random.choice([15000, 20000, 25000, 30000, 35000, 45000, 50000])
    costo = round(precio * random.uniform(0.35, 0.60), 2)

    productos.append({
        "id_producto": i,
        "nombre_producto": f"{categoria} modelo {i:02d}",
        "categoria": categoria,
        "material": random.choice(materiales),
        "precio_referencia": precio,
        "costo_referencia": costo
    })

# Inconsistencia intencional para corregir en Power Query.
productos[4]["categoria"] = "aretes "

guardar_csv(
    "dim_producto.csv",
    ["id_producto", "nombre_producto", "categoria", "material",
     "precio_referencia", "costo_referencia"],
    productos
)


# --------------------------------------------------
# 3. DIMENSION DE CLIENTES
# --------------------------------------------------

clientes = []

nombres = [
    "Laura", "Valentina", "Camila", "Daniela", "Sofia",
    "Mariana", "Isabella", "Gabriela", "Natalia", "Paula",
    "Andrea", "Juliana", "Sara", "Manuela", "Luciana"
]

apellidos = [
    "Rodriguez", "Martinez", "Garcia", "Lopez", "Gomez",
    "Ramirez", "Torres", "Diaz", "Morales", "Castro"
]

for i in range(1, 201):
    clientes.append({
        "id_cliente": i,
        "nombre_cliente": (
            f"{random.choice(nombres)} "
            f"{random.choice(apellidos)}"
        ),
        "ciudad": random.choice(["Neiva", "Campoalegre", "Rivera"]),
        "segmento": random.choice(["Nuevo", "Frecuente", "Recurrente"])
    })

guardar_csv(
    "dim_cliente.csv",
    ["id_cliente", "nombre_cliente", "ciudad", "segmento"],
    clientes
)


# --------------------------------------------------
# 4. DIMENSION DE CANALES
# --------------------------------------------------

canales = [
    {
        "id_canal": 1,
        "nombre_canal": "Instagram",
        "tipo_canal": "Redes sociales"
    },
    {
        "id_canal": 2,
        "nombre_canal": "WhatsApp",
        "tipo_canal": "Redes sociales"
    },
    {
        "id_canal": 3,
        "nombre_canal": "Venta directa",
        "tipo_canal": "Presencial"
    }
]

guardar_csv(
    "dim_canal.csv",
    ["id_canal", "nombre_canal", "tipo_canal"],
    canales
)


# --------------------------------------------------
# 5. TABLA DE HECHOS: VENTAS
# --------------------------------------------------

ventas = []

for i in range(1, 1501):
    producto = random.choice(productos)
    cliente = random.choice(clientes)
    canal = random.choice(canales)

    dia = random.choice(fechas)
    fecha_venta = date.fromisoformat(dia["fecha"])

    cantidad = random.randint(1, 4)
    precio_unitario = producto["precio_referencia"]
    costo_unitario = producto["costo_referencia"]

    descuento = round(
        random.choice([0, 0, 0, 1000, 2000, 3000]),
        2
    )

    ventas.append({
        "id_detalle_venta": i,
        "id_venta": f"V-{i:05d}",
        "id_fecha": dia["id_fecha"],
        "fecha_venta": fecha_venta.strftime("%Y-%m-%d"),
        "id_producto": producto["id_producto"],
        "id_cliente": cliente["id_cliente"],
        "id_canal": canal["id_canal"],
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "descuento": descuento,
        "costo_unitario": costo_unitario
    })

# Inconsistencia intencional de formato de fecha.
ventas[10]["fecha_venta"] = date.fromisoformat(
    ventas[10]["fecha_venta"]
).strftime("%d/%m/%Y")

# Duplicado intencional para identificar y tratar.
venta_duplicada = ventas[20].copy()
ventas.append(venta_duplicada)

guardar_csv(
    "fact_ventas.csv",
    [
        "id_detalle_venta",
        "id_venta",
        "id_fecha",
        "fecha_venta",
        "id_producto",
        "id_cliente",
        "id_canal",
        "cantidad",
        "precio_unitario",
        "descuento",
        "costo_unitario"
    ],
    ventas
)


# --------------------------------------------------
# 6. RESUMEN DE GENERACION
# --------------------------------------------------

print("\nGENERACION FINALIZADA")
print("------------------------------")
print(f"Fechas: {len(fechas)}")
print(f"Productos: {len(productos)}")
print(f"Clientes: {len(clientes)}")
print(f"Canales: {len(canales)}")
print(f"Ventas: {len(ventas)}")
print("Periodo: enero a diciembre de 2025")
print("Errores intencionales: duplicado e inconsistencias")
print("------------------------------")