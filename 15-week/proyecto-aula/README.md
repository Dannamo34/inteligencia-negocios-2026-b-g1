
# Proyecto de Aula – Inteligencia de Negocios
## Nani Accesorios

### 1. Información general

| Campo | Información |
|---|---|
| Institución | Corporación Universitaria del Huila – CORHUILA |
| Programa | Ingeniería de Sistemas |
| Asignatura | Electiva Inteligencia de Negocios |
| Periodo académico | 2026-B |
| Corte | Corte 3 |
| Docente | Jesús Ariel González Bonilla |
| Proyecto | Nani Accesorios |
| Integrante 1 | Danna Michelle Morales Losada |
| Integrante 2 | Alison Fernanda Puentes Avendaño |
| Ubicación de la empresa | Neiva, Huila |
| Herramienta de análisis | Microsoft Power BI |
| Periodo de análisis | 1 de enero al 31 de diciembre de 2025 |

---

### 2. Descripción de la empresa

Nani Accesorios es una empresa ficticia ubicada en Neiva, Huila, dedicada a la comercialización de accesorios como aretes, collares, pulseras y anillos.

La empresa ofrece productos elaborados con materiales como miyuki, mostacilla, acero, perlas y otros elementos de bisutería. Sus ventas se realizan principalmente mediante redes sociales, mensajería y atención directa a los clientes.

Para este proyecto se construye un conjunto de datos sintéticos que representa las operaciones comerciales de la empresa durante el año 2025. La información permite analizar las ventas, los descuentos, los costos y la rentabilidad de los productos y canales comerciales.

### 3. Problema empresarial

Nani Accesorios no cuenta con un proceso centralizado de análisis que permita identificar con claridad cuáles productos y canales generan mayor rentabilidad.

Las decisiones sobre descuentos y promoción de productos se pueden tomar considerando principalmente el volumen de ventas, sin evaluar suficientemente los costos y el efecto de los descuentos sobre el margen bruto.

Esta situación puede ocasionar que la empresa impulse productos o canales que generan muchas ventas, pero que dejan una ganancia menor. Por esta razón, se plantea implementar una solución de Inteligencia de Negocios que integre los datos y facilite la toma de decisiones comerciales.

### 4. Pregunta de negocio

¿Qué categorías y canales de venta generaron mayor margen bruto en Nani Accesorios durante 2025, y dónde conviene concentrar o ajustar los descuentos para aprovechar las temporadas de mayor demanda?

### 5. Objetivos

#### 5.1. Objetivo general

Desarrollar una solución de Inteligencia de Negocios para analizar las ventas, los costos, los descuentos y el margen bruto de Nani Accesorios durante 2025, con el propósito de identificar oportunidades de mejora en las decisiones comerciales.

#### 5.2. Objetivos específicos

- Integrar la información comercial en un modelo de datos estructurado.
- Generar datos sintéticos que representen las operaciones de la empresa durante los doce meses de 2025.
- Identificar y corregir problemas de calidad de datos mediante Power Query.
- Construir un modelo dimensional tipo estrella.
- Crear medidas DAX para analizar ventas, costos, descuentos y rentabilidad.
- Diseñar un tablero interactivo en Power BI para apoyar las decisiones sobre productos, canales y temporadas.

### 6. Indicador principal y métricas

El indicador principal del proyecto es el margen bruto porcentual.

**Margen bruto (%)**

```text
Margen bruto (%) =
((Ventas netas - Costo de ventas) / Ventas netas) * 100
```

Se utilizarán los siguientes indicadores complementarios:

| Indicador | Descripción |
|---|---|
| Ventas brutas | Valor total de los productos antes de descuentos |
| Descuentos | Valor monetario descontado en las ventas |
| Ventas netas | Ventas brutas menos descuentos |
| Costo de ventas | Costo de los productos vendidos |
| Margen bruto | Ventas netas menos costo de ventas |
| Margen bruto (%) | Porcentaje de margen respecto a las ventas netas |
| Unidades vendidas | Cantidad total de productos vendidos |

### 7. Alcance del proyecto

El proyecto comprende el análisis de las operaciones comerciales ficticias de Nani Accesorios durante el año 2025.

Se analizarán:

- Las ventas por mes y temporada.
- El comportamiento de las categorías y productos.
- La participación de los canales de venta.
- Los descuentos aplicados.
- Los costos y el margen bruto.
- Las oportunidades para mejorar las decisiones comerciales.

El proyecto no utiliza información financiera real de una empresa. Todos los datos son sintéticos y se generan con fines académicos.

### 8. Modelo de datos

Se utiliza un modelo dimensional tipo estrella compuesto por una tabla de hechos y cuatro dimensiones.

**Tabla de hechos:**

- `fact_ventas`: contiene los detalles de las transacciones comerciales, las cantidades, los precios, los descuentos y los costos.

**Tablas de dimensiones:**

- `dim_fecha`: contiene la información del calendario.
- `dim_producto`: contiene los productos, sus categorías, materiales, precios y costos de referencia.
- `dim_cliente`: contiene información ficticia de los clientes.
- `dim_canal`: contiene los canales utilizados para realizar las ventas.

**Relaciones del modelo:**

- `dim_fecha[id_fecha]` → `fact_ventas[id_fecha]`
- `dim_producto[id_producto]` → `fact_ventas[id_producto]`
- `dim_cliente[id_cliente]` → `fact_ventas[id_cliente]`
- `dim_canal[id_canal]` → `fact_ventas[id_canal]`

Cada dimensión se relaciona con la tabla de hechos mediante una relación de uno a varios (1:N).

**Granularidad:** cada registro de `fact_ventas` representa una línea o detalle de producto perteneciente a una transacción. Por esta razón, un mismo `id_venta` puede aparecer en varias filas cuando una compra contiene diferentes productos.

El detalle de cada línea se identifica mediante `id_detalle_venta`.

### 9. Generación de los datos

Los datos se generan mediante el script `data/generar_datos.py`, desarrollado en Python.

El generador crea cinco archivos CSV:

| Archivo | Contenido |
|---|---|
| `dim_fecha.csv` | Calendario de los 365 días de 2025 |
| `dim_producto.csv` | Catálogo de productos |
| `dim_cliente.csv` | Clientes ficticios |
| `dim_canal.csv` | Canales de venta |
| `fact_ventas.csv` | Detalles de las transacciones comerciales |

Las reglas utilizadas para generar los datos son:

1. El periodo de análisis comprende desde enero hasta diciembre de 2025.
2. Se generan 30 productos distribuidos entre las cuatro categorías comerciales.
3. Se generan 200 clientes ficticios.
4. Se utilizan tres canales: Instagram, WhatsApp y venta directa.
5. Se generan 1.200 transacciones, con una o varias líneas de productos por compra.
6. Algunos productos tienen mayor probabilidad de venta para representar productos estrella.
7. Mayo, septiembre y diciembre tienen una mayor demanda simulada por las temporadas comerciales.
8. Los descuentos varían según el canal de venta para permitir analizar su efecto sobre el margen bruto.
9. Los identificadores de las dimensiones se utilizan como claves de relación con la tabla de hechos.
10. Se incluyen problemas intencionales de calidad para demostrar su tratamiento en Power Query.

La generación utiliza una semilla aleatoria fija para que los resultados puedan reproducirse al ejecutar nuevamente el script.

### 10. Calidad y transformación de los datos

El proyecto incorpora problemas intencionales de calidad que serán identificados y corregidos mediante Power Query.

| Problema | Tratamiento esperado |
|---|---|
| Filas duplicadas | Identificar y eliminar duplicados exactos |
| Fechas con formatos diferentes | Convertirlas a un formato de fecha uniforme |
| Categorías con espacios o escritura irregular | Limpiar espacios y estandarizar los nombres |

El generador incluye varios casos de cada problema para que el proceso de limpieza sea visible y pueda documentarse mediante evidencias de antes y después.

La validación inicial se realiza con `data/validar_datos.py`. Este script comprueba la estructura de los archivos, las claves, las relaciones entre las tablas, las cantidades de registros y los problemas intencionales.

Los archivos CSV originales se conservan como fuente de datos. La limpieza para el análisis se realiza en Power Query.

### 11. Herramientas utilizadas

- **Python:** generación y validación de datos sintéticos.
- **CSV:** almacenamiento de las tablas de datos.
- **Visual Studio Code:** edición y organización del código y la documentación.
- **Power Query:** limpieza y transformación de los datos.
- **Power BI Desktop:** construcción del modelo, medidas DAX y tablero interactivo.
- **Git y GitHub:** control de versiones y trabajo colaborativo.

### 12. Diseño del tablero en Power BI

El tablero estará organizado en tres páginas:

#### 12.1. Resumen

Responderá a la pregunta: ¿Cómo le fue al negocio durante 2025?

Incluirá:

- Margen bruto porcentual.
- Ventas netas.
- Costo de ventas.
- Unidades vendidas.
- Tendencia mensual de ventas.

#### 12.2. Productos

Responderá a la pregunta: ¿Qué categorías y productos dejan más margen?

Incluirá:

- Ventas por categoría.
- Margen bruto por categoría.
- Comparación entre productos.
- Jerarquía de categoría a producto con navegación drill-down.

#### 12.3. Canales

Responderá a la pregunta: ¿Qué canal conviene impulsar?

Incluirá:

- Ventas por canal.
- Margen bruto por canal.
- Descuentos por canal.
- Comparación del efecto de los descuentos sobre la rentabilidad.

El tablero contará con segmentadores para facilitar el análisis por mes y canal, además de interacciones entre sus visualizaciones.

### 13. Recomendación empresarial

La recomendación inicial consiste en revisar la política de descuentos antes de las temporadas de mayor demanda, comparando las ventas netas, los costos y el margen bruto de cada canal.

La persona responsable de la administración comercial de Nani Accesorios deberá revisar los resultados y definir los descuentos que se aplicarán en cada canal. Esta revisión debe realizarse al menos dos semanas antes de las temporadas de Día de la Madre, Amor y Amistad y Navidad.

La decisión definitiva sobre qué productos y canales deben recibir mayor promoción se establecerá con los resultados comprobados del tablero de Power BI, evitando recomendar descuentos únicamente por el volumen de ventas.

### 14. Overview & Insights

Nani Accesorios is a fictional accessories business located in Neiva, Colombia. This project analyzes its simulated sales operations during the year 2025. The dataset includes products, customers, sales channels, dates, quantities, prices, costs, and discounts. A star schema is used to organize the information and support business analysis. Python is used to generate and validate the synthetic data. Power Query is used to identify and correct data quality issues before analysis. Power BI is used to calculate business indicators and build an interactive dashboard. The dashboard compares product categories, sales channels, monthly performance, and gross profit margins. These results will support decisions about product promotions and discount strategies during important commercial seasons.

**Nota:** las conclusiones cuantitativas y los hallazgos específicos se completarán después de construir y comprobar el tablero en Power BI.

### 15. Integrantes del proyecto

**Danna Michelle Morales Losada**

Responsable de la construcción y documentación de los componentes del proyecto, generación de datos y análisis de información.

**Alison Fernanda Puentes Avendaño**

Responsable de participar en la preparación de datos, validación, construcción del análisis y documentación del proyecto.

Ambas integrantes participan en el desarrollo y revisión de la solución de Inteligencia de Negocios.
