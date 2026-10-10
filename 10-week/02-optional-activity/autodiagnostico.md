# Autodiagnóstico: Corte 2

## Temas que domino

- [x] **Cargar un archivo y abrir Power Query.** Conecté el CSV con Obtener datos, ajusté la codificación 1252 y usé Transformar datos antes de cargar.
- [x] **Diferencia entre Extract, Transform y Load.** Sé qué hace cada fase y en qué parte de Power BI se hace cada una.
- [x] **Limpiar texto.** Aplico Recortar y Limpiar sobre las columnas de texto.
- [x] **Quitar duplicados.** Entiendo que hay que excluir el `Row ID`, porque es único por fila y no deja detectar repetidos reales.
- [x] **Cambiar tipos de dato.** Convertí ventas, descuento y ganancia a número decimal, y las fechas a tipo fecha.
- [x] **Construir una matriz por categoría.** Sé poner `Category` en filas y las medidas en valores.

## Temas que debo repasar

- [ ] **Granularidad.** La entiendo, pero me cuesta definirla rápido en un caso nuevo. Debo practicar identificando qué representa una fila antes de calcular.
- [ ] **Fechas con configuración regional.** Al principio no tenía claro por qué Power BI confunde día y mes. Debo repasar cuándo usar Inglés (EE. UU.) y cuándo Español (Colombia).
- [ ] **Anular dinamización de columnas.** La apliqué solo en teoría para el caso del enunciado, porque Superstore no tiene un mes por columna. Debo practicarla con un archivo que sí lo tenga.
- [ ] **Precios en texto con formato colombiano.** Debo practicar el reemplazo de `.` y `,` para no dañar los valores.
- [ ] **Sintaxis DAX y nombres de tablas.** Me apareció el error "No se encuentra la tabla". Aprendí que los nombres con espacios o guiones van entre comillas simples, pero debo repasarlo para no equivocarme en el parcial.
- [ ] **Medida vs. columna calculada.** Sé la diferencia general, pero me falta práctica decidiendo cuál usar.
- [ ] **Contexto de filtro.** Entiendo que una medida cambia según la categoría, pero debo profundizar en cómo se evalúa `DIVIDE` dentro de la matriz.

## Lo que me costó

Lo más difícil fue entender que en Superstore cada fila es una línea de producto y no un pedido completo. Al principio pensé en usar `COUNTROWS` para el ticket promedio, pero eso daría un valor incorrecto. Entendí que debo contar pedidos distintos con `DISTINCTCOUNT(Order ID)`. También me costó el error de nombre de tabla en las medidas, que resolví renombrando la tabla a `Ventas`.

## Plan de repaso antes del parcial

1. **Anular dinamización y precios en texto:** conseguir un CSV con un mes por columna y precios como texto, y aplicar la receta completa en el orden correcto.
2. **DAX:** reescribir las tres medidas desde cero, sin copiar, y probarlas por categoría, por región y por año.
3. **Fechas y granularidad:** practicar con 3 o 4 archivos distintos: identificar qué es una fila y unificar fechas de formatos mezclados.
4. **Simulacro:** hacer la actividad completa de nuevo en 30 minutos, para medir qué tan fluido me quedó el flujo ETL y las medidas.