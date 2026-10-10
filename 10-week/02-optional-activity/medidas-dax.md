# Medidas DAX propuestas

Tabla del modelo: `Ventas` (columnas usadas: `Sales`, `Order ID`, `Category`).

## Medidas para el caso de Superstore

```dax
Total Ventas = SUM(Ventas[Sales])
```
Suma todas las ventas en el contexto del filtro actual (por ejemplo, una categoría).

```dax
Num Pedidos = DISTINCTCOUNT(Ventas[Order ID])
```
Cuenta pedidos únicos. No se usa `COUNTROWS` porque un pedido tiene varias filas.

```dax
Ticket Promedio = DIVIDE([Total Ventas], [Num Pedidos])
```
Ventas promedio por pedido. `DIVIDE` evita el error por división entre cero.

## Medidas para el caso del enunciado (después de anular dinamización)

Tras el paso 7 de la receta, la tabla tiene las columnas `Mes` y `Monto`:

```dax
Total Ventas = SUM(Ventas[Monto])
```

Si existe una columna de identificador de venta o pedido:
```dax
Num Ventas = DISTINCTCOUNT(Ventas[IdVenta])
```
Si no existe, cada fila es una venta:
```dax
Num Ventas = COUNTROWS(Ventas)
```
```dax
Ticket Promedio = DIVIDE([Total Ventas], [Num Ventas])
```

Si el monto no viene hecho y hay cantidad y precio unitario:
```dax
Total Ventas = SUMX(Ventas, Ventas[Cantidad] * Ventas[Precio])
```

## Uso por categoría

Matriz con `Category` en Filas y `Total Ventas`, `Num Pedidos` y `Ticket Promedio` en Valores.


**Observación:** los pedidos por categoría no suman el total, porque un mismo pedido puede contener productos de varias categorías.