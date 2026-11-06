
import csv
import random
from datetime import date, timedelta
from pathlib import Path

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

random.seed(2026)

CARPETA = Path(__file__).resolve().parent

ANIO = 2025
NUM_CLIENTES = 200
NUM_TRANSACCIONES = 1200

MESES = [
    "enero", "febrero", "marzo", "abril",
    "mayo", "junio", "julio", "agosto",
    "septiembre", "octubre", "noviembre", "diciembre"
]

# Mayor demanda en temporadas comerciales.
PESO_MENSUAL = {
    1: 1.0,
    2: 0.9,
    3: 1.0,
    4: 1.0,
    5: 1.9,   # Día de la Madre
    6: 1.0,
    7: 0.9,
    8: 1.0,
    9: 1.8,   # Amor y Amistad
    10: 1.0,
    11: 1.2,
    12: 2.0   # Navidad
}

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def guardar_csv(nombre_archivo, encabezados, registros):
    ruta = CARPETA / nombre_archivo

    with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=encabezados,
            delimiter=","
        )
        escritor.writeheader()
        escritor.writerows(registros)

    print(f"Archivo generado: {ruta.name} ({len(registros)} registros)")


def generar_fechas():
    fechas = []
    fecha_actual = date(ANIO, 1, 1)
    fecha_final = date(ANIO, 12, 31)

    while fecha_actual <= fecha_final:
        fechas.append(fecha_actual)
        fecha_actual += timedelta(days=1)

    return fechas


def seleccionar_fecha(fechas):
    pesos = [PESO_MENSUAL[fecha.month] for fecha in fechas]
    return random.choices(fechas, weights=pesos, k=1)[0]


# ============================================================
# DIMENSIÓN FECHA
# ============================================================

def crear_dim_fecha():
    fechas = generar_fechas()
    registros = []

    for fecha in fechas:
        registros.append({
            "id_fecha": int(fecha.strftime("%Y%m%d")),
            "fecha": fecha.strftime("%Y-%m-%d"),
            "dia": fecha.day,
            "mes": fecha.month,
            "nombre_mes": MESES[fecha.month - 1],
            "trimestre": ((fecha.month - 1) // 3) + 1,
            "anio": fecha.year
        })

    return registros


# ============================================================
# DIMENSIÓN PRODUCTO
# ============================================================

def crear_dim_producto():
    productos = []

    catalogo = {
        "Aretes": [
            "Aretes Luna", "Aretes Estrella", "Aretes Perla",
            "Aretes Flor", "Aretes Corazón", "Aretes Dorados",
            "Aretes Mariposa", "Aretes Cristal"
        ],
        "Collares": [
            "Collar Sol", "Collar Perlas", "Collar Inicial",
            "Collar Corazón", "Collar Minimalista",
            "Collar Dorado", "Collar Elegante"
        ],
        "Pulseras": [
            "Pulsera Miyuki", "Pulsera Dorada", "Pulsera Perlas",
            "Pulsera Corazón", "Pulsera Tejida", "Pulsera Cristal",
            "Pulsera Estrella", "Pulsera Ajustable"
        ],
        "Anillos": [
            "Anillo Dorado", "Anillo Plata", "Anillo Corazón",
            "Anillo Perla", "Anillo Ajustable",
            "Anillo Elegante", "Anillo Minimalista"
        ]
    }

    id_producto = 1

    for categoria, nombres in catalogo.items():
        for nombre in nombres:
            precio = random.choice([
                18000, 20000, 22000, 25000, 28000,
                30000, 35000, 38000, 42000, 45000
            ])

            porcentaje_costo = random.uniform(0.35, 0.58)
            costo = round(precio * porcentaje_costo, 2)

            productos.append({
                "id_producto": id_producto,
                "nombre_producto": nombre,
                "categoria": categoria,
                "material": random.choice([
                    "Miyuki", "Mostacilla", "Acero",
                    "Bisutería", "Perlas", "Cristal"
                ]),
                "precio_referencia": precio,
                "costo_referencia": costo
            })

            id_producto += 1

    # Tres errores intencionales de escritura para Power Query.
    productos[2]["categoria"] = "aretes "
    productos[10]["categoria"] = "COLLARES"
    productos[22]["categoria"] = " Pulseras"

    return productos


# ============================================================
# DIMENSIÓN CLIENTE
# ============================================================

def crear_dim_cliente():
    nombres = [
        "Valentina", "Camila", "Laura", "Mariana", "Daniela",
        "Isabella", "Gabriela", "Sofía", "Luciana", "Natalia",
        "Paula", "Andrea", "Juliana", "Sara", "Manuela",
        "Alejandra", "Carolina", "María", "Antonia", "Victoria"
    ]

    apellidos = [
        "Rojas", "García", "Martínez", "López", "Rodríguez",
        "Pérez", "Gómez", "Ramírez", "Torres", "Díaz",
        "Morales", "Castro", "Vargas", "Mendoza", "Ortiz"
    ]

    clientes = []

    for i in range(1, NUM_CLIENTES + 1):
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"

        clientes.append({
            "id_cliente": i,
            "nombre_cliente": nombre,
            "ciudad": random.choices(
                ["Neiva", "Campoalegre", "Rivera", "Palermo", "Garzón"],
                weights=[65, 12, 8, 8, 7],
                k=1
            )[0],
            "segmento": random.choice([
                "Nuevo", "Frecuente", "Recurrente"
            ])
        })

    return clientes


# ============================================================
# DIMENSIÓN CANAL
# ============================================================

def crear_dim_canal():
    return [
        {
            "id_canal": 1,
            "nombre_canal": "Instagram",
            "tipo_canal": "Redes sociales"
        },
        {
            "id_canal": 2,
            "nombre_canal": "WhatsApp",
            "tipo_canal": "Mensajería"
        },
        {
            "id_canal": 3,
            "nombre_canal": "Venta directa",
            "tipo_canal": "Presencial"
        }
    ]


# ============================================================
# GENERACIÓN DE VENTAS
# ============================================================

def crear_fact_ventas(productos, clientes, canales, fechas):
    ventas = []
    id_detalle = 1

    # Los productos estrella tienen mayor probabilidad de venta.
    pesos_productos = []

    for producto in productos:
        if producto["id_producto"] in [1, 9, 17, 25]:
            pesos_productos.append(5)
        else:
            pesos_productos.append(1)

    for numero_venta in range(1, NUM_TRANSACCIONES + 1):

        fecha = seleccionar_fecha(fechas)
        cliente = random.choice(clientes)

        # WhatsApp concentra más transacciones, pero tiene
        # descuentos mayores y, por tanto, menor margen.
        canal = random.choices(
            canales,
            weights=[35, 50, 15],
            k=1
        )[0]

        # Cada transacción puede contener entre 1 y 3 productos.
        cantidad_lineas = random.choices(
            [1, 2, 3],
            weights=[25, 50, 25],
            k=1
        )[0]

        productos_venta = random.choices(
            productos,
            weights=pesos_productos,
            k=1
        )

        # Evitar repetir un mismo producto dentro de una venta.
        productos_disponibles = productos.copy()
        productos_venta = []

        for _ in range(min(cantidad_lineas, len(productos_disponibles))):
            pesos_disponibles = [
                5 if p["id_producto"] in [1, 9, 17, 25] else 1
                for p in productos_disponibles
            ]

            seleccionado = random.choices(
                productos_disponibles,
                weights=pesos_disponibles,
                k=1
            )[0]

            productos_venta.append(seleccionado)
            productos_disponibles.remove(seleccionado)

        for producto in productos_venta:
            cantidad = random.randint(1, 4)
            precio_unitario = float(producto["precio_referencia"])
            costo_unitario = float(producto["costo_referencia"])

            subtotal = cantidad * precio_unitario

            if canal["nombre_canal"] == "WhatsApp":
                porcentaje_descuento = random.uniform(0.12, 0.25)
            elif canal["nombre_canal"] == "Instagram":
                porcentaje_descuento = random.uniform(0.05, 0.12)
            else:
                porcentaje_descuento = random.uniform(0.00, 0.05)

            descuento = round(subtotal * porcentaje_descuento, 2)

            ventas.append({
                "id_detalle_venta": id_detalle,
                "id_venta": numero_venta,
                "id_fecha": int(fecha.strftime("%Y%m%d")),
                "fecha_venta": fecha.strftime("%Y-%m-%d"),
                "id_producto": producto["id_producto"],
                "id_cliente": cliente["id_cliente"],
                "id_canal": canal["id_canal"],
                "cantidad": cantidad,
                "precio_unitario": precio_unitario,
                "descuento": descuento,
                "costo_unitario": costo_unitario
            })

            id_detalle += 1

    # Cinco fechas con formatos diferentes: errores intencionales
    # que deberán corregirse mediante Power Query.
    formatos_fecha = [
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%d.%m.%Y"
    ]

    indices_fecha = random.sample(range(len(ventas)), 5)

    for indice, formato in zip(indices_fecha, formatos_fecha):
        fecha_original = date.fromisoformat(
            ventas[indice]["fecha_venta"]
        )
        ventas[indice]["fecha_venta"] = fecha_original.strftime(formato)

    # Cinco filas duplicadas intencionalmente para practicar
    # la eliminación de duplicados en Power Query.
    filas_duplicadas = random.sample(ventas, 5)

    for fila in filas_duplicadas:
        ventas.append(fila.copy())

    return ventas


# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

def main():
    print("\n==============================================")
    print("GENERACIÓN DE DATOS - NANI ACCESORIOS")
    print("Periodo de análisis: 2025")
    print("==============================================\n")

    dim_fecha = crear_dim_fecha()
    dim_producto = crear_dim_producto()
    dim_cliente = crear_dim_cliente()
    dim_canal = crear_dim_canal()

    fechas = generar_fechas()

    fact_ventas = crear_fact_ventas(
        dim_producto,
        dim_cliente,
        dim_canal,
        fechas
    )

    guardar_csv(
        "dim_fecha.csv",
        [
            "id_fecha", "fecha", "dia", "mes",
            "nombre_mes", "trimestre", "anio"
        ],
        dim_fecha
    )

    guardar_csv(
        "dim_producto.csv",
        [
            "id_producto", "nombre_producto", "categoria",
            "material", "precio_referencia", "costo_referencia"
        ],
        dim_producto
    )

    guardar_csv(
        "dim_cliente.csv",
        [
            "id_cliente", "nombre_cliente", "ciudad", "segmento"
        ],
        dim_cliente
    )

    guardar_csv(
        "dim_canal.csv",
        [
            "id_canal", "nombre_canal", "tipo_canal"
        ],
        dim_canal
    )

    guardar_csv(
        "fact_ventas.csv",
        [
            "id_detalle_venta", "id_venta", "id_fecha",
            "fecha_venta", "id_producto", "id_cliente",
            "id_canal", "cantidad", "precio_unitario",
            "descuento", "costo_unitario"
        ],
        fact_ventas
    )

    print("\n==============================================")
    print("RESUMEN DE GENERACIÓN")
    print("==============================================")
    print(f"Fechas generadas: {len(dim_fecha)}")
    print(f"Productos generados: {len(dim_producto)}")
    print(f"Clientes generados: {len(dim_cliente)}")
    print(f"Canales generados: {len(dim_canal)}")
    print(f"Transacciones generadas: {NUM_TRANSACCIONES}")
    print(f"Líneas de venta, incluidos duplicados: {len(fact_ventas)}")
    print("Errores intencionales de categoría: 3")
    print("Fechas con formato irregular: 5")
    print("Filas duplicadas intencionalmente: 5")
    print("\nGeneración terminada correctamente.")
    print("==============================================\n")


if __name__ == "__main__":
    main()
