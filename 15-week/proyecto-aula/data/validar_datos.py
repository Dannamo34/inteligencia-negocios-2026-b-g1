
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

# ============================================================
# CONFIGURACIÓN
# ============================================================

CARPETA = Path(__file__).resolve().parent

ARCHIVOS = {
    "fecha": "dim_fecha.csv",
    "producto": "dim_producto.csv",
    "cliente": "dim_cliente.csv",
    "canal": "dim_canal.csv",
    "ventas": "fact_ventas.csv"
}

MESES_VALIDOS = {
    "enero", "febrero", "marzo", "abril",
    "mayo", "junio", "julio", "agosto",
    "septiembre", "octubre", "noviembre", "diciembre"
}

CATEGORIAS_VALIDAS = {
    "Aretes", "Collares", "Pulseras", "Anillos"
}

FORMATOS_FECHA = [
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%Y/%m/%d",
    "%d-%m-%Y",
    "%m/%d/%Y",
    "%d.%m.%Y"
]


# ============================================================
# LECTURA DE ARCHIVOS
# ============================================================

def leer_csv(nombre):
    ruta = CARPETA / nombre

    if not ruta.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {nombre}"
        )

    with open(ruta, "r", newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def convertir_fecha(valor):
    for formato in FORMATOS_FECHA:
        try:
            return datetime.strptime(valor, formato).date()
        except ValueError:
            continue

    return None


def verificar_columnas(registros, columnas, nombre):
    if not registros:
        print(f"[ERROR] {nombre}: el archivo está vacío.")
        return False

    columnas_archivo = set(registros[0].keys())
    faltantes = set(columnas) - columnas_archivo

    if faltantes:
        print(
            f"[ERROR] {nombre}: faltan columnas: "
            f"{', '.join(sorted(faltantes))}"
        )
        return False

    print(f"[OK] {nombre}: estructura de columnas correcta.")
    return True


def convertir_ids(registros, campo):
    return {
        int(registro[campo])
        for registro in registros
        if registro.get(campo, "").strip()
    }


# ============================================================
# VALIDACIÓN DE DIMENSIONES
# ============================================================

def validar_dim_fecha(fechas):
    print("\n--- DIM_FECHA ---")

    columnas = [
        "id_fecha", "fecha", "dia", "mes",
        "nombre_mes", "trimestre", "anio"
    ]

    verificar_columnas(fechas, columnas, "dim_fecha.csv")

    fechas_repetidas = [
        valor for valor, cantidad in Counter(
            fila["id_fecha"] for fila in fechas
        ).items()
        if cantidad > 1
    ]

    meses_en_ingles = [
        fila["nombre_mes"]
        for fila in fechas
        if fila["nombre_mes"].lower() not in MESES_VALIDOS
    ]

    fechas_fuera_del_anio = [
        fila for fila in fechas
        if fila["anio"] != "2025"
    ]

    print(f"Registros: {len(fechas)}")
    print(f"Claves de fecha repetidas: {len(fechas_repetidas)}")
    print(f"Meses que no están en español: {len(meses_en_ingles)}")
    print(f"Registros fuera de 2025: {len(fechas_fuera_del_anio)}")

    if len(fechas) == 365 and not fechas_repetidas:
        print("[OK] Calendario de 2025 completo y sin claves repetidas.")
    else:
        print("[REVISAR] El calendario debe contener 365 fechas únicas.")


def validar_dim_producto(productos):
    print("\n--- DIM_PRODUCTO ---")

    columnas = [
        "id_producto", "nombre_producto", "categoria",
        "material", "precio_referencia", "costo_referencia"
    ]

    verificar_columnas(productos, columnas, "dim_producto.csv")

    ids = [fila["id_producto"] for fila in productos]
    ids_repetidos = [
        valor for valor, cantidad in Counter(ids).items()
        if cantidad > 1
    ]

    categorias_irregulares = [
        fila["categoria"]
        for fila in productos
        if fila["categoria"].strip().title() not in CATEGORIAS_VALIDAS
        or fila["categoria"] != fila["categoria"].strip().title()
    ]

    distribucion = Counter(
        fila["categoria"].strip().title()
        for fila in productos
    )

    print(f"Productos: {len(productos)}")
    print(f"Claves de producto repetidas: {len(ids_repetidos)}")
    print(f"Categorías con escritura irregular: {len(categorias_irregulares)}")
    print("Distribución por categoría:")

    for categoria, cantidad in sorted(distribucion.items()):
        print(f"  {categoria}: {cantidad}")

    if not ids_repetidos:
        print("[OK] Las claves de productos son únicas.")

    if categorias_irregulares:
        print(
            "[AVISO] Se detectaron categorías intencionalmente "
            "mal escritas para practicar Power Query."
        )


def validar_dim_cliente(clientes):
    print("\n--- DIM_CLIENTE ---")

    columnas = [
        "id_cliente", "nombre_cliente", "ciudad", "segmento"
    ]

    verificar_columnas(clientes, columnas, "dim_cliente.csv")

    ids = [fila["id_cliente"] for fila in clientes]
    repetidos = [
        valor for valor, cantidad in Counter(ids).items()
        if cantidad > 1
    ]

    print(f"Clientes: {len(clientes)}")
    print(f"Claves de cliente repetidas: {len(repetidos)}")

    if not repetidos:
        print("[OK] Las claves de clientes son únicas.")


def validar_dim_canal(canales):
    print("\n--- DIM_CANAL ---")

    columnas = [
        "id_canal", "nombre_canal", "tipo_canal"
    ]

    verificar_columnas(canales, columnas, "dim_canal.csv")

    ids = [fila["id_canal"] for fila in canales]
    repetidos = [
        valor for valor, cantidad in Counter(ids).items()
        if cantidad > 1
    ]

    print(f"Canales: {len(canales)}")
    print(f"Claves de canal repetidas: {len(repetidos)}")

    if not repetidos:
        print("[OK] Las claves de canales son únicas.")


# ============================================================
# VALIDACIÓN DE LA TABLA DE HECHOS
# ============================================================

def validar_fact_ventas(ventas, fechas, productos, clientes, canales):
    print("\n--- FACT_VENTAS ---")

    columnas = [
        "id_detalle_venta", "id_venta", "id_fecha",
        "fecha_venta", "id_producto", "id_cliente",
        "id_canal", "cantidad", "precio_unitario",
        "descuento", "costo_unitario"
    ]

    verificar_columnas(ventas, columnas, "fact_ventas.csv")

    print(f"Líneas de venta: {len(ventas)}")

    # Duplicados exactos intencionales.
    filas = [tuple(sorted(fila.items())) for fila in ventas]
    cantidades_filas = Counter(filas)

    duplicados_exactos = sum(
        cantidad - 1
        for cantidad in cantidades_filas.values()
        if cantidad > 1
    )

    print(f"Filas duplicadas exactas: {duplicados_exactos}")

    # Identificadores de dimensiones.
    ids_fecha = convertir_ids(fechas, "id_fecha")
    ids_producto = convertir_ids(productos, "id_producto")
    ids_cliente = convertir_ids(clientes, "id_cliente")
    ids_canal = convertir_ids(canales, "id_canal")

    # Integridad referencial.
    referencias_fecha = [
        fila["id_fecha"] for fila in ventas
        if int(fila["id_fecha"]) not in ids_fecha
    ]

    referencias_producto = [
        fila["id_producto"] for fila in ventas
        if int(fila["id_producto"]) not in ids_producto
    ]

    referencias_cliente = [
        fila["id_cliente"] for fila in ventas
        if int(fila["id_cliente"]) not in ids_cliente
    ]

    referencias_canal = [
        fila["id_canal"] for fila in ventas
        if int(fila["id_canal"]) not in ids_canal
    ]

    print("\nIntegridad referencial:")
    print(f"Referencias de fecha sin correspondencia: {len(referencias_fecha)}")
    print(f"Referencias de producto sin correspondencia: {len(referencias_producto)}")
    print(f"Referencias de cliente sin correspondencia: {len(referencias_cliente)}")
    print(f"Referencias de canal sin correspondencia: {len(referencias_canal)}")

    # Identificadores de detalle repetidos.
    ids_detalle = [fila["id_detalle_venta"] for fila in ventas]
    detalles_repetidos = [
        valor for valor, cantidad in Counter(ids_detalle).items()
        if cantidad > 1
    ]

    print(
        "\nClaves de detalle repetidas "
        "(se esperan por los duplicados intencionales): "
        f"{len(detalles_repetidos)}"
    )

    # Una venta debe tener varias líneas en algunos casos.
    lineas_por_venta = Counter(
        fila["id_venta"] for fila in ventas
    )

    ventas_multiproducto = sum(
        1 for cantidad in lineas_por_venta.values()
        if cantidad > 1
    )

    print(f"Transacciones identificadas: {len(lineas_por_venta)}")
    print(f"Transacciones con varias líneas: {ventas_multiproducto}")

    # Fechas irregulares intencionales.
    fechas_irregulares = [
        fila["fecha_venta"]
        for fila in ventas
        if convertir_fecha(fila["fecha_venta"]) is not None
        and len(fila["fecha_venta"]) != 10
        or (
            convertir_fecha(fila["fecha_venta"]) is not None
            and fila["fecha_venta"] != convertir_fecha(
                fila["fecha_venta"]
            ).strftime("%Y-%m-%d")
        )
    ]

    fechas_no_validas = [
        fila["fecha_venta"]
        for fila in ventas
        if convertir_fecha(fila["fecha_venta"]) is None
    ]

    print(f"Fechas con formato irregular: {len(fechas_irregulares)}")
    print(f"Fechas que no se pueden interpretar: {len(fechas_no_validas)}")

    # Valores numéricos.
    valores_negativos = 0

    for fila in ventas:
        cantidad = float(fila["cantidad"])
        precio = float(fila["precio_unitario"])
        descuento = float(fila["descuento"])
        costo = float(fila["costo_unitario"])

        if (
            cantidad <= 0
            or precio <= 0
            or costo <= 0
            or descuento < 0
            or descuento > cantidad * precio
        ):
            valores_negativos += 1

    print(f"Registros con valores numéricos inválidos: {valores_negativos}")

    if len(ventas) >= 1000:
        print("[OK] Se cumple el mínimo de 1.000 registros de hechos.")
    else:
        print("[ERROR] No se cumple el mínimo de 1.000 registros.")

    if ventas_multiproducto > 0:
        print("[OK] Existen transacciones con varias líneas de productos.")
    else:
        print("[ERROR] No se encontraron ventas con varias líneas.")

    if not any([
        referencias_fecha,
        referencias_producto,
        referencias_cliente,
        referencias_canal
    ]):
        print("[OK] Las claves de las dimensiones cruzan correctamente.")

    if duplicados_exactos > 0:
        print(
            "[AVISO] Los duplicados son intencionales y deben "
            "eliminarse en Power Query."
        )

    if fechas_irregulares:
        print(
            "[AVISO] Las fechas con formatos diferentes son "
            "intencionales y deben normalizarse en Power Query."
        )

    if valores_negativos:
        print("[ERROR] Hay valores numéricos que requieren revisión.")


# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

def main():
    print("\n================================================")
    print("VALIDACIÓN DE DATOS - NANI ACCESORIOS")
    print("Periodo de análisis: 2025")
    print("================================================")

    try:
        fechas = leer_csv(ARCHIVOS["fecha"])
        productos = leer_csv(ARCHIVOS["producto"])
        clientes = leer_csv(ARCHIVOS["cliente"])
        canales = leer_csv(ARCHIVOS["canal"])
        ventas = leer_csv(ARCHIVOS["ventas"])

    except (FileNotFoundError, KeyError) as error:
        print(f"\n[ERROR] {error}")
        print("Ejecute primero generar_datos.py.")
        return

    validar_dim_fecha(fechas)
    validar_dim_producto(productos)
    validar_dim_cliente(clientes)
    validar_dim_canal(canales)

    validar_fact_ventas(
        ventas,
        fechas,
        productos,
        clientes,
        canales
    )

    print("\n================================================")
    print("VALIDACIÓN FINALIZADA")
    print("================================================")
    print("Revise los avisos de calidad y conserve los")
    print("errores intencionales para limpiarlos en Power Query.")
    print("================================================\n")


if __name__ == "__main__":
    main()
