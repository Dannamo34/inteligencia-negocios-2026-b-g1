# Corte 1 - Inteligencia de Negocios

## Objetivos

- Autoevaluar los conceptos aprendidos durante el Corte 1.
- Resolver un caso práctico de modelado estrella.
- Identificar los temas que domino y aquellos que debo repasar antes del parcial.

---

# 1. Resumen de conceptos del Corte 1

## Cadena del dato

La cadena del dato representa el proceso mediante el cual los datos se convierten en información útil para tomar decisiones. Este proceso comienza con la **captura de datos**, continúa con su **almacenamiento, transformación y análisis**, y finalmente permite generar información y conocimiento para apoyar la toma de decisiones.

De forma general, la cadena puede representarse así:

**Datos → Información → Conocimiento → Decisiones**

Por ejemplo, una farmacia registra cada venta realizada. Estos datos pueden transformarse en información sobre cuáles productos se venden más, posteriormente generar conocimiento sobre el comportamiento de los clientes y finalmente ayudar a tomar decisiones como aumentar el inventario de determinados productos.

---

## KPI

Un **KPI (Key Performance Indicator)** es un indicador clave de rendimiento que permite medir el cumplimiento de un objetivo específico de una organización.

Los KPI deben estar relacionados con objetivos y permitir evaluar el desempeño de un proceso.

Algunos ejemplos son:

- Ventas totales por mes.
- Número de productos vendidos.
- Ticket promedio.
- Porcentaje de crecimiento de las ventas.
- Cantidad de ventas por sucursal.

Por ejemplo, si una farmacia tiene como objetivo aumentar sus ventas mensuales, un KPI podría ser el **porcentaje de crecimiento de las ventas respecto al mes anterior**.

---

## OLTP vs OLAP

### OLTP

**OLTP (Online Transaction Processing)** se utiliza para gestionar las operaciones diarias de una organización.

Su objetivo principal es registrar y procesar transacciones de manera rápida y consistente.

Ejemplos:

- Registrar una venta.
- Registrar un pago.
- Actualizar el inventario.
- Crear una factura.
- Registrar un cliente.

Las bases de datos OLTP normalmente están diseñadas para operaciones frecuentes de inserción, actualización y consulta de datos.

### OLAP

**OLAP (Online Analytical Processing)** está orientado al análisis de grandes cantidades de información.

Permite consultar datos históricos y analizarlos desde diferentes perspectivas para apoyar la toma de decisiones.

Ejemplos:

- Analizar las ventas por mes.
- Comparar las ventas entre sucursales.
- Identificar los productos más vendidos.
- Analizar el comportamiento de las ventas durante varios años.

### Diferencia principal

| OLTP | OLAP |
|---|---|
| Orientado a transacciones | Orientado al análisis |
| Maneja operaciones del día a día | Maneja información histórica |
| Muchas operaciones pequeñas | Consultas analíticas complejas |
| Inserta y actualiza datos constantemente | Principalmente consulta datos |
| Ejemplo: sistema de ventas | Ejemplo: Data Warehouse |

---

## Data Warehouse

Un **Data Warehouse** es un repositorio centralizado de datos diseñado para realizar análisis y apoyar la toma de decisiones.

Integra información proveniente de diferentes fuentes y conserva datos históricos que pueden ser analizados mediante herramientas de inteligencia de negocios.

Entre sus principales características se encuentran:

- Integra información de diferentes fuentes.
- Conserva información histórica.
- Está orientado al análisis.
- Facilita la generación de reportes.
- Permite calcular indicadores y analizar tendencias.

Por ejemplo, una cadena de farmacias puede utilizar un Data Warehouse para almacenar información histórica de sus ventas, productos y sucursales y posteriormente analizar cómo han evolucionado sus ventas durante varios meses o años.

---

## Modelo estrella

El **modelo estrella** es una técnica de modelado utilizada principalmente en Data Warehouses.

Está compuesto por una **tabla de hechos** ubicada en el centro y varias **dimensiones** relacionadas con ella.

La tabla de hechos contiene los eventos que se desean analizar y las medidas numéricas asociadas a esos eventos.

Las dimensiones contienen información descriptiva que permite analizar los hechos desde diferentes perspectivas.

Su estructura recibe el nombre de modelo estrella porque visualmente la tabla de hechos se encuentra en el centro y las dimensiones alrededor de ella.

Ejemplo general:

```text
                    DIM_PRODUCTO
                         |
                         |
DIM_SUCURSAL ---- TABLA_HECHOS ---- DIM_TIEMPO
                         |
                         |
                    DIM_CLIENTE

2. Caso práctico: Cadena de farmacias
Enunciado

Una cadena de farmacias quiere analizar sus ventas por:

Producto.
Sucursal.
Mes.

Para solucionar esta necesidad se propone utilizar un modelo estrella, donde la tabla central representa las ventas y las dimensiones permiten analizarlas desde diferentes perspectivas.

Modelo estrella propuesto
                         DIM_PRODUCTO
                              |
                              |
                              |
DIM_SUCURSAL ----------- FACT_VENTAS ----------- DIM_TIEMPO
                              |
                              |
                              |
                         DIM_CLIENTE

Para el requerimiento mínimo del caso se utilizan Producto, Sucursal y Tiempo. La dimensión Cliente puede agregarse si la organización necesita analizar las ventas por cliente.

Tabla de hechos: FACT_VENTAS

La tabla de hechos representa cada evento de venta realizado en una sucursal.

Medidas

Las principales medidas propuestas son:

cantidad_vendida: cantidad de unidades vendidas.
precio_unitario: precio de venta de cada unidad.
descuento: valor descontado en la venta.
total_venta: valor total de la venta.
Claves
producto_id
sucursal_id
tiempo_id

Estas claves permiten relacionar cada venta con sus respectivas dimensiones.

Ejemplo:

producto_id	sucursal_id	tiempo_id	cantidad_vendida	precio_unitario	descuento	total_venta
101	5	202608	3	15000	0	45000
205	2	202608	2	25000	5000	45000
101	5	202609	5	15000	2000	73000
Dimensión DIM_PRODUCTO

Permite conocer las características de los productos vendidos.

Atributos
producto_id
nombre_producto
categoria
marca
presentacion
laboratorio
tipo_producto

Ejemplo:

producto_id	nombre_producto	categoria	marca	presentacion	laboratorio
101	Acetaminofén	Analgésico	Genérica	Tabletas	Laboratorio A
205	Vitamina C	Vitaminas	Marca X	Tabletas	Laboratorio B
Dimensión DIM_SUCURSAL

Permite analizar las ventas según la sucursal donde se realizó la operación.

Atributos
sucursal_id
nombre_sucursal
ciudad
direccion
zona
tipo_sucursal

Ejemplo:

sucursal_id	nombre_sucursal	ciudad	zona
1	Sucursal Centro	Neiva	Centro
2	Sucursal Norte	Neiva	Norte
3	Sucursal Sur	Neiva	Sur
Dimensión DIM_TIEMPO

Permite analizar las ventas a través del tiempo.

Atributos
tiempo_id
fecha
dia
mes
nombre_mes
trimestre
año

Ejemplo:

tiempo_id	fecha	mes	nombre_mes	trimestre	año
20260801	2026-08-01	8	Agosto	3	2026
20260802	2026-08-02	8	Agosto	3	2026
20260901	2026-09-01	9	Septiembre	3	2026
Relación entre hechos y dimensiones

La estructura final del modelo sería:

                         DIM_PRODUCTO
                         ------------
                         producto_id
                         nombre_producto
                         categoria
                         marca
                         presentacion
                         laboratorio
                              |
                              |
                              |
DIM_SUCURSAL ----------- FACT_VENTAS ----------- DIM_TIEMPO
------------             -----------             ----------
sucursal_id              producto_id             tiempo_id
nombre_sucursal          sucursal_id             fecha
ciudad                   tiempo_id               dia
direccion                cantidad_vendida        mes
zona                     precio_unitario         nombre_mes
                         descuento               trimestre
                         total_venta             año
Justificación del modelo

Se seleccionó un modelo estrella porque la necesidad principal de la cadena de farmacias es analizar las ventas desde diferentes perspectivas.

La tabla FACT_VENTAS representa el evento principal del negocio: una venta realizada. En ella se almacenan las medidas que pueden ser analizadas, como la cantidad vendida y el total de la venta.

La dimensión DIM_PRODUCTO permite responder preguntas relacionadas con los productos, por ejemplo:

¿Qué producto se vende más?
¿Qué categoría genera mayores ventas?
¿Qué marca tiene mejores resultados?

La dimensión DIM_SUCURSAL permite analizar el rendimiento de cada establecimiento:

¿Qué sucursal vende más?
¿Qué ciudad genera mayores ingresos?
¿Qué zona tiene mayor volumen de ventas?

La dimensión DIM_TIEMPO permite realizar análisis históricos:

¿Cuál fue el mes con mayores ventas?
¿Cómo han evolucionado las ventas?
¿Qué trimestre tuvo mejores resultados?
¿Cómo se comportan las ventas año tras año?

Por lo tanto, el modelo permite combinar las dimensiones para realizar análisis como:

Ventas por producto + sucursal + mes

Por ejemplo:

¿Cuánto dinero generó la venta de Acetaminofén en la sucursal Centro durante agosto de 2026?

El modelo estrella facilita este tipo de consultas porque las dimensiones contienen la información descriptiva y la tabla de hechos contiene las medidas que serán analizadas.