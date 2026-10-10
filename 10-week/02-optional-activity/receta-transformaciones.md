# Receta de transformaciones (Power Query)

## Caso del enunciado

CSV de ventas con: **precios como texto**, **fechas mezcladas**, **duplicados** y **un mes por columna**.

Orden de la receta y justificación:

| # | Transformación | Cómo se hace en Power Query | Por qué en este orden |
|---|---|---|---|
| 1 | Promover encabezados | Inicio → Usar primera fila como encabezados | Sin nombres de columna correctos no se puede referenciar nada después |
| 2 | Quitar filas vacías | Inicio → Quitar filas → Quitar filas en blanco | Evita errores en los pasos de tipo y de duplicados |
| 3 | Limpiar texto | Transformar → Formato → Recortar y Limpiar (y Poner en mayúscula cada palabra) | Debe ir **antes** de quitar duplicados, si no "Balón " y "balón" cuentan como distintos |
| 4 | Precios de texto a número | Reemplazar valores (quitar `$` y espacios; en formato colombiano quitar `.` de miles y cambiar `,` por `.`) y luego Cambiar tipo a Número decimal | Sin tipo numérico no se puede sumar ni promediar |
| 5 | Unificar fechas mezcladas | Cambiar tipo → Usar configuración regional → Fecha (con la región correcta); las filas con error se separan por delimitador o con columna condicional por cada formato | Fechas bien tipadas permiten agrupar por mes y año sin errores |
| 6 | Quitar duplicados | Seleccionar las columnas que identifican el registro (excluyendo cualquier ID autonumérico) → clic derecho → Quitar duplicados | Se hace con texto y valores ya normalizados, para detectar todos los repetidos reales |
| 7 | Anular dinamización de meses | Seleccionar las columnas que NO son meses → clic derecho → Anular dinamización de otras columnas; renombrar *Atributo* a `Mes` y *Valor* a `Monto` | Pasa de "un mes por columna" a "una fila por mes", formato necesario para las medidas |
| 8 | Tipos finales y errores | Asignar tipo a cada columna; reemplazar o filtrar errores y nulos | Garantiza datos consistentes antes de cargar |
| 9 | Cargar | Inicio → Cerrar y aplicar | Envía la tabla limpia al modelo |

## Práctica realizada con Superstore

Como el dataset Superstore ya trae precios numéricos y no tiene meses en columnas, apliqué los pasos 1, 2, 3, 5, 6 y 8:

- **Fechas:** `Order Date` y `Ship Date` venían como texto en formato mes/día/año de EE. UU. Se convirtieron con Usar configuración regional → Fecha → Inglés (Estados Unidos).
- **Duplicados:** se quitaron seleccionando todas las columnas **menos `Row ID`**, porque `Row ID` es único por fila e impediría detectar repetidos.
- **Resultado:** [FILAS_ANTES] filas antes y [FILAS_DESPUES] después de quitar duplicados.