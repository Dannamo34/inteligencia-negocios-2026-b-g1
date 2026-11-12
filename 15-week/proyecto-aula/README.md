
# Proyecto de Aula – Inteligencia de Negocios
# Nani Accesorios

## 1. Información general

| Campo | Información |
|---|---|
| Institución | Corporación Universitaria del Huila – CORHUILA |
| Programa | Ingeniería de Sistemas e Ingeniería Ambiental |
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

## 2. Descripción de la empresa

Nani Accesorios es una empresa ficticia ubicada en Neiva, Huila, dedicada a la comercialización de accesorios como aretes, collares, pulseras y anillos.

La empresa ofrece productos elaborados con materiales como miyuki, mostacilla, acero, perlas y otros elementos de bisutería. Sus ventas se realizan principalmente mediante redes sociales, mensajería y atención directa a los clientes.

Para este proyecto se construyó un conjunto de datos sintéticos que representa las operaciones comerciales de la empresa durante el año 2025. La información permite analizar las ventas, los descuentos, los costos y la utilidad de los productos y canales comerciales.

## 3. Problema empresarial

Nani Accesorios no cuenta con un proceso centralizado de análisis que permita identificar con claridad cuáles productos y canales generan mejores resultados comerciales.

Las decisiones sobre descuentos y promoción de productos pueden tomarse considerando principalmente el volumen de ventas, sin evaluar suficientemente los costos y la utilidad obtenida.

Esta situación puede ocasionar que la empresa impulse productos o canales que generan muchas ventas, pero que dejan una ganancia menor.

Por esta razón, se plantea implementar una solución de Inteligencia de Negocios que integre los datos y facilite la toma de decisiones comerciales.

## 4. Pregunta de negocio

¿Qué categorías y canales de venta generan mejores resultados comerciales en Nani Accesorios durante 2025, y cómo se pueden utilizar los datos de ventas, descuentos y utilidad para mejorar las decisiones comerciales?

## 5. Objetivos

### 5.1. Objetivo general

Desarrollar una solución de Inteligencia de Negocios para analizar las ventas, los costos, los descuentos y la utilidad de Nani Accesorios durante 2025, con el propósito de identificar oportunidades de mejora en las decisiones comerciales.

### 5.2. Objetivos específicos

- Integrar la información comercial en un modelo de datos estructurado.
- Generar datos sintéticos que representen las operaciones de la empresa durante los doce meses de 2025.
- Identificar y corregir problemas de calidad de datos mediante Power Query.
- Construir un modelo dimensional tipo estrella.
- Crear medidas DAX para analizar las ventas, los descuentos, los costos y la utilidad.
- Diseñar un tablero interactivo en Power BI para apoyar las decisiones sobre productos, canales y comportamiento comercial.

## 6. Indicadores del proyecto

Para analizar el comportamiento comercial se utilizan los siguientes indicadores:

| Indicador | Descripción |
|---|---|
| Ventas brutas | Valor total de las ventas antes de aplicar descuentos |
| Descuentos | Valor de los descuentos aplicados |
| Ventas netas | Valor de las ventas después de los descuentos |
| Costos | Valor asociado al costo de los productos vendidos |
| Utilidad | Resultado de las ventas después de considerar los costos |
| Cantidad vendida | Total de unidades comercializadas |
| Número de ventas | Cantidad de ventas registradas |

El análisis de estos indicadores permite comparar los resultados por producto, categoría, canal y periodo.

El margen bruto porcentual también hace parte del enfoque de análisis del proyecto. Su cálculo y resultado deberán comprobarse con las medidas definitivas del archivo Power BI.

## 7. Alcance del proyecto

El proyecto comprende el análisis de las operaciones comerciales ficticias de Nani Accesorios durante el año 2025.

Se analizan los siguientes aspectos:

- Las ventas durante los diferentes meses del año.
- El comportamiento de las categorías y productos.
- La participación de los canales de venta.
- Los descuentos aplicados.
- Los costos y la utilidad.
- El comportamiento de los indicadores mediante filtros interactivos.

El proyecto no utiliza información financiera real de una empresa. Todos los datos son sintéticos y se generan con fines académicos.

## 8. Modelo de datos

Se construyó un modelo dimensional tipo estrella compuesto por una tabla de hechos y cuatro dimensiones.

### 8.1. Tabla de hechos

- `fact_ventas`: contiene los detalles de las transacciones comerciales, las cantidades, los precios, los descuentos y los costos.

### 8.2. Tablas de dimensiones

- `dim_fecha`: contiene la información del calendario.
- `dim_producto`: contiene los productos, sus categorías, materiales, precios y costos de referencia.
- `dim_cliente`: contiene información ficticia de los clientes.
- `dim_canal`: contiene los canales utilizados para realizar las ventas.

### 8.3. Relaciones del modelo

Las relaciones establecidas en Power BI son:

- `dim_cliente` → `fact_ventas`
- `dim_producto` → `fact_ventas`
- `dim_fecha` → `fact_ventas`
- `dim_canal` → `fact_ventas`

Cada dimensión proporciona información relacionada con los registros de la tabla de hechos y permite realizar análisis desde diferentes perspectivas.

La estructura corresponde a un modelo estrella, donde la tabla de hechos centraliza las operaciones comerciales y las dimensiones permiten clasificarlas.

### 8.4. Granularidad

Cada registro de `fact_ventas` representa una línea o detalle de producto perteneciente a una transacción. Por esta razón, un mismo identificador de venta puede aparecer en varias filas cuando una compra contiene diferentes productos.

El detalle de cada línea se identifica mediante `id_detalle_venta`.

## 9. Generación de los datos

Los datos del proyecto se generan mediante un script desarrollado en Python.

El conjunto de datos está compuesto por cinco archivos CSV:

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
8. Los descuentos varían según el canal de venta.
9. Los identificadores de las dimensiones se utilizan como claves de relación con la tabla de hechos.
10. Se incluyen problemas intencionales de calidad para demostrar su tratamiento en Power Query.

La generación utiliza una semilla aleatoria fija para que los resultados puedan reproducirse al ejecutar nuevamente el script.

## 10. Calidad y transformación de los datos

Los datos originales contienen problemas intencionales de calidad que fueron tratados mediante Power Query.

Durante el proceso se realizaron las siguientes actividades:

- Importación de las cinco tablas CSV en Power BI.
- Verificación de los tipos de datos de las columnas.
- Asignación de números enteros a los identificadores y cantidades.
- Asignación de números decimales a los valores monetarios.
- Configuración del tipo fecha para las fechas de venta.
- Limpieza de inconsistencias en las categorías.
- Eliminación de espacios innecesarios.

El proceso permitió preparar la información para su utilización en el modelo de datos y en las visualizaciones.

Los archivos CSV originales se conservan como fuente de datos, mientras que las transformaciones se realizan en Power Query.

## 11. Herramientas utilizadas

| Herramienta | Utilización |
|---|---|
| Python | Generación y validación de datos sintéticos |
| CSV | Almacenamiento de las tablas de datos |
| Visual Studio Code | Edición y organización del código y la documentación |
| Power Query | Limpieza y transformación de los datos |
| Power BI Desktop | Construcción del modelo, medidas DAX y tablero interactivo |
| Git y GitHub | Control de versiones y almacenamiento del proyecto |

## 12. Desarrollo del tablero en Power BI

El tablero de Power BI está organizado en tres páginas principales: Resumen, Productos y Canales.

### 12.1. Página Resumen

La página Resumen presenta los principales indicadores del negocio mediante tarjetas, gráficos y filtros interactivos.

Su propósito es facilitar una visión general del comportamiento comercial de Nani Accesorios durante 2025.

### 12.2. Página Productos

La página Productos permite analizar las ventas y utilidades por producto y categoría.

Esta página facilita la comparación del comportamiento de los productos y permite identificar las categorías que tienen mayor participación en los resultados comerciales.

### 12.3. Página Canales

La página Canales muestra el comportamiento de las ventas según los medios de comercialización utilizados por la empresa.

Permite comparar los resultados de los diferentes canales y analizar su participación en las operaciones comerciales.

## 13. Medidas DAX

Para el análisis de la información se desarrollaron las siguientes medidas en Power BI:

| Medida | Descripción |
|---|---|
| Ventas Brutas | Calcula el valor total de las ventas antes de descuentos |
| Descuentos | Calcula el valor total descontado |
| Ventas Netas | Representa las ventas después de aplicar descuentos |
| Costos | Permite analizar el costo de los productos vendidos |
| Utilidad | Permite analizar el resultado económico de las ventas |
| Cantidad Vendida | Calcula las unidades comercializadas |
| Número de Ventas | Permite analizar la cantidad de ventas registradas |

Estas medidas se utilizan en las tarjetas y visualizaciones del tablero para facilitar el análisis de la información.

Las fórmulas DAX exactas se documentarán de acuerdo con las expresiones implementadas en el archivo `.pbix`.

## 14. Pruebas de funcionamiento e interactividad

Se realizaron pruebas para comprobar que los filtros del tablero actualizan los indicadores y las visualizaciones de acuerdo con las selecciones realizadas.

### 14.1. Prueba por canal

Se aplicó el filtro correspondiente al canal Instagram para verificar la actualización automática de los indicadores y gráficos.

### 14.2. Prueba por categoría

Se seleccionó la categoría Aretes para comprobar el comportamiento de las ventas y utilidades correspondientes a esta selección.

### 14.3. Prueba por ciudad

Se aplicó un filtro de ciudad para comprobar la actualización dinámica de los indicadores.

Estas pruebas permitieron verificar el funcionamiento de los filtros y la interacción entre los datos del modelo.

## 15. Resultados e insights

El tablero permite analizar el comportamiento comercial de Nani Accesorios desde tres perspectivas: el resumen general, los productos y los canales de venta.

A partir de las visualizaciones y los indicadores se pueden estudiar:

1. El comportamiento de las ventas durante el periodo de análisis.
2. La participación de las categorías y productos en las ventas.
3. Las utilidades obtenidas por producto y categoría.
4. El comportamiento de los diferentes canales de comercialización.
5. Los cambios en los indicadores al seleccionar un canal, una categoría o una ciudad.

Los resultados cuantitativos específicos se incorporarán después de verificar las cifras definitivas del tablero de Power BI.

## 16. Conclusiones

1. La implementación del modelo estrella permitió organizar adecuadamente la información y mejorar la estructura para realizar los análisis comerciales.

2. Las medidas DAX facilitaron el cálculo de indicadores clave como ventas netas, utilidad y cantidad vendida.

3. El dashboard desarrollado permite analizar rápidamente el comportamiento comercial de la empresa mediante visualizaciones interactivas.

4. Los filtros implementados demostraron la correcta relación entre las tablas y la actualización dinámica de la información.

5. El uso de Power Query permitió preparar los datos mediante la revisión de tipos de datos y la limpieza de inconsistencias antes de realizar el análisis.

## 17. Diccionario de datos

El modelo utiliza cinco tablas principales:

| Tabla | Descripción | Clave principal |
|---|---|---|
| `dim_fecha` | Información del calendario de 2025 | `id_fecha` |
| `dim_producto` | Información de los productos comercializados | `id_producto` |
| `dim_cliente` | Información ficticia de los clientes | `id_cliente` |
| `dim_canal` | Información de los canales de venta | `id_canal` |
| `fact_ventas` | Detalles de las transacciones comerciales | `id_detalle_venta` |

Las claves foráneas de la tabla de hechos permiten relacionar las ventas con las dimensiones de fecha, producto, cliente y canal.

El detalle de los campos, tipos de datos y descripciones se organizará en el archivo `diccionario-datos.md`.

## 18. Evidencias del desarrollo en Power BI

Las evidencias fotográficas permiten comprobar las actividades realizadas durante el desarrollo del proyecto.

### 18.1. Importación y transformación de datos

Se documenta la importación de las cinco tablas y el proceso de limpieza realizado en Power Query.

- [Importación de las tablas](evidencias/01-power-query/1.png)
- [Limpieza y transformación de datos](evidencias/01-power-query/3.png)

### 18.2. Modelo estrella

Se presenta la estructura del modelo dimensional y las relaciones entre las tablas.

- [Modelo estrella implementado](evidencias/02-modelo/1.png)

### 18.3. Medidas DAX

Se presenta la evidencia de las medidas creadas para realizar los cálculos de los indicadores comerciales.

- [Medidas DAX implementadas](evidencias/03-medidas-dax/2.png)

### 18.4. Páginas del tablero

Se presentan las tres páginas desarrolladas en Power BI.

- [Página Resumen](evidencias/04-tablero/1.png)
- [Página Productos](evidencias/04-tablero/2.png)
- [Página Canales](evidencias/04-tablero/3.png)

### 18.5. Pruebas de funcionamiento

Se presentan las pruebas realizadas para verificar la actualización dinámica de los indicadores y gráficos.

- [Prueba de filtro por canal Instagram](evidencias/05-prueba-clic/1.png)
- [Prueba de filtro por categoría Aretes](evidencias/05-prueba-clic/2.png)
- [Prueba de filtro por ciudad](evidencias/05-prueba-clic/3.png)

### 18.6. Evidencia fotográfica completa

El documento consolidado de evidencias se encontrará en:

## 19. Archivo del proyecto Power BI

El archivo principal del análisis se almacenará en la carpeta `powerbi`.

**Archivo:** `Nani_Accesorios.pbix`

[Consultar archivo Power BI](power-bi/proyecto_final.pbix.zip)

Este archivo contiene el modelo de datos, las transformaciones realizadas en Power Query, las medidas DAX y las páginas del tablero interactivo.

Para visualizarlo se requiere Microsoft Power BI Desktop.

## 20. Integrantes del proyecto

### Danna Michelle Morales Losada

Participante del desarrollo de la solución de Inteligencia de Negocios, generación de datos, preparación de la información, análisis y documentación del proyecto.

### Alison Fernanda Puentes Avendaño

Participante del desarrollo de la solución de Inteligencia de Negocios, preparación de datos, validación, construcción del análisis y documentación del proyecto.

Ambas integrantes participan en el desarrollo y revisión de la solución de Inteligencia de Negocios.