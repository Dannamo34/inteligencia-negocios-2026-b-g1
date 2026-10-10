# Resumen del Corte 2: Inteligencia de Negocios

## 1. Granularidad

La granularidad es el nivel de detalle que representa **una fila** de la tabla. Definirla primero es clave, porque de ella depende qué se puede contar y cómo se calculan las medidas.

En el dataset Superstore, cada fila es una **línea de producto dentro de un pedido**, no el pedido completo. Un mismo `Order ID` puede aparecer en varias filas. Por eso, para el ticket promedio se cuentan pedidos distintos y no filas.

## 2. ETL con Power Query

**Extract (extraer):** se conecta la fuente (CSV o Excel) con Obtener datos. Se revisa la codificación (1252 para tildes y ñ) y se elige *Transformar datos* para no cargar datos sucios.

**Transform (transformar):** se limpia y se da forma a los datos, en orden:
1. Promover encabezados y quitar filas vacías.
2. Limpiar texto (recortar espacios y caracteres no imprimibles).
3. Convertir tipos (precios de texto a número, fechas de texto a fecha usando la configuración regional correcta).
4. Quitar duplicados.
5. Anular dinamización de columnas (cuando hay un mes por columna) para tener una fila por mes.
6. Revisar errores y nulos.

**Load (cargar):** *Cerrar y aplicar* envía la tabla limpia al modelo de Power BI, donde se crean las medidas.

El orden importa: por ejemplo, se normaliza el texto antes de quitar duplicados, porque "Balón " y "balón" parecerían filas distintas.

## 3. Medidas DAX

Una medida es un cálculo que se evalúa según el contexto del filtro (por ejemplo, por categoría).

```dax
Total Ventas = SUM(Ventas[Sales])
Num Pedidos = DISTINCTCOUNT(Ventas[Order ID])
Ticket Promedio = DIVIDE([Total Ventas], [Num Pedidos])
```

- `SUM` suma la columna en el contexto actual.
- `DISTINCTCOUNT` cuenta pedidos únicos.
- `DIVIDE` divide de forma segura (evita error por división entre cero).

**Diferencia clave:** una *columna calculada* se calcula fila a fila al cargar; una *medida* se calcula al vuelo según los filtros del informe.