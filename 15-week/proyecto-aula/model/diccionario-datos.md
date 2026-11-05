# Diccionario de datos - Nani Accesorios

## 1. Descripción

Este documento define la estructura de datos que se utilizará
para desarrollar el proyecto de inteligencia de negocios de
Nani Accesorios.

El modelo permitirá analizar las ventas, los productos, los
clientes, los canales comerciales y el comportamiento de los
indicadores de rentabilidad.

La información será sintética y tendrá fines exclusivamente
académicos.

## 2. Periodo de análisis

- Fecha inicial: 01 de enero de 2025.
- Fecha final: 31 de diciembre de 2025.
- Duración: 12 meses.
- Registros mínimos de la tabla de hechos: 1.000.

## 3. Modelo dimensional

Se utilizará un modelo estrella compuesto por una tabla de
hechos y cuatro dimensiones.

### Tabla de hechos

#### FACT_VENTAS

Granularidad: cada registro representa un producto vendido
dentro de una transacción comercial.

| Campo | Tipo de dato | Descripción |
|---|---|---|
| id_detalle_venta | Entero | Identificador único del detalle de venta. |
| id_venta | Texto | Identificador de la transacción. |
| id_fecha | Entero | Clave relacionada con la dimensión fecha. |
| id_producto | Entero | Clave relacionada con la dimensión producto. |
| id_cliente | Entero | Clave relacionada con la dimensión cliente. |
| id_canal | Entero | Clave relacionada con la dimensión canal. |
| cantidad | Entero | Unidades vendidas. |
| precio_unitario | Decimal | Precio de venta por unidad. |
| descuento | Decimal | Valor total del descuento aplicado a la línea. |
| costo_unitario | Decimal | Costo de adquisición por unidad. |

### Dimensiones

#### DIM_FECHA

| Campo | Tipo de dato | Descripción |
|---|---|---|
| id_fecha | Entero | Clave de fecha en formato AAAAMMDD. |
| fecha | Fecha | Fecha completa. |
| dia | Entero | Día del mes. |
| mes | Entero | Número del mes. |
| nombre_mes | Texto | Nombre del mes. |
| trimestre | Texto | Trimestre del año. |
| anio | Entero | Año correspondiente. |

#### DIM_PRODUCTO

| Campo | Tipo de dato | Descripción |
|---|---|---|
| id_producto | Entero | Identificador del producto. |
| nombre_producto | Texto | Nombre comercial del producto. |
| categoria | Texto | Aretes, collares, pulseras o anillos. |
| material | Texto | Material principal del accesorio. |
| precio_referencia | Decimal | Precio de referencia del producto. |
| costo_referencia | Decimal | Costo de referencia del producto. |

#### DIM_CLIENTE

| Campo | Tipo de dato | Descripción |
|---|---|---|
| id_cliente | Entero | Identificador del cliente. |
| nombre_cliente | Texto | Nombre ficticio del cliente. |
| ciudad | Texto | Ciudad de procedencia. |
| segmento | Texto | Clasificación comercial del cliente. |

#### DIM_CANAL

| Campo | Tipo de dato | Descripción |
|---|---|---|
| id_canal | Entero | Identificador del canal. |
| nombre_canal | Texto | Canal de comercialización. |
| tipo_canal | Texto | Clasificación del canal. |

Los canales contemplados serán redes sociales y venta directa.

## 4. Relaciones del modelo

La tabla FACT_VENTAS se relacionará con las cuatro dimensiones:

- FACT_VENTAS[id_fecha] con DIM_FECHA[id_fecha].
- FACT_VENTAS[id_producto] con DIM_PRODUCTO[id_producto].
- FACT_VENTAS[id_cliente] con DIM_CLIENTE[id_cliente].
- FACT_VENTAS[id_canal] con DIM_CANAL[id_canal].

Cada dimensión tendrá una relación de uno a muchos con
la tabla de hechos.

## 5. Indicadores que se calcularán

### Ventas brutas

Suma de cantidad multiplicada por precio unitario.

### Ventas netas

Ventas brutas menos descuentos.

### Costo de ventas

Suma de cantidad multiplicada por costo unitario.

### Margen bruto

Ventas netas menos costo de ventas.

### Margen bruto porcentual

(Margen bruto / Ventas netas) * 100.

### Unidades vendidas

Suma de las cantidades comercializadas.

## 6. Reglas de calidad de datos

Durante el proceso de extracción y transformación se
incluirán dos problemas controlados:

1. Registros duplicados que deberán identificarse y tratarse.
2. Inconsistencias en fechas y nombres de categorías que
   deberán estandarizarse.

Los problemas se documentarán antes y después de la limpieza.

## 7. Consideraciones

- Los datos serán ficticios y no representarán clientes reales.
- La tabla FACT_VENTAS tendrá al menos 1.000 registros.
- El periodo de análisis comprenderá doce meses.
- Las claves de las dimensiones deberán coincidir con las
  utilizadas en la tabla de hechos.
- Los cálculos de ventas y rentabilidad se realizarán
  utilizando las medidas definidas en Power BI.