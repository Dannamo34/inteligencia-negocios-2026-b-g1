
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

carpeta = Path(__file__).parent

productos = [
    ("P001", "Aretes", "Accesorios"),
    ("P002", "Collares", "Accesorios"),
    ("P003", "Pulseras", "Accesorios"),
    ("P004", "Anillos", "Accesorios"),
    ("P005", "Bolsos", "Complementos"),
    ("P006", "Carteras", "Complementos"),
]

canales = ["Tienda física", "Instagram", "WhatsApp", "Facebook"]

with open(carpeta / "ventas.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow([
        "VentaID", "Fecha", "ProductoID", "Producto",
        "Categoria", "Canal", "Cantidad", "PrecioUnitario",
        "TotalVenta"
    ])

    inicio = date(2025, 1, 1)

    for i in range(1, 501):
        fecha = inicio + timedelta(days=random.randint(0, 364))
        producto_id, producto, categoria = random.choice(productos)
        canal = random.choice(canales)
        cantidad = random.randint(1, 5)
        precio = random.choice([15000, 20000, 25000, 30000, 35000, 40000, 50000])
        total = cantidad * precio

        escritor.writerow([
            i, fecha.isoformat(), producto_id, producto,
            categoria, canal, cantidad, precio, total
        ])

print("Archivo ventas.csv generado correctamente.")
