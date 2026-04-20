# Análisis de Ventas

## Instrucciones
Entrega: Presenta tus resultados en un archivo de texto o una hoja de cálculo. Detalla cada paso del análisis y los resultados obtenidos. Asegúrate de incluir:

* [La lista de ventas original](#1-lista-de-ventas-original)
* [Los ingresos totales generados](#2-ingresos-totales)
* [El producto más vendido y su cantidad total vendida](#3-producto-más-vendido)
* [El precio promedio de venta por producto](#4-precio-promedio-por-producto)
* [Los ingresos totales por día](#5-ingresos-totales-por-día)
* [El resumen de ventas por producto](#6-resumen-de-ventas)

## 1. Lista de Ventas Original
La lista de ventas se generó mediante el archivo "seed_core_3.py" y el resultado se almacena en el archivo "ventas.json".

```
[
    {
        "fecha": "2025-08-12",
        "producto": "teddy cat",
        "cantidad": 6,
        "precio": 200
    },
    {
        "fecha": "2025-07-03",
        "producto": "Smartphone",
        "cantidad": 2,
        "precio": 1200
    },
    {
        "fecha": "2025-10-01",
        "producto": "Berserk Deluxe Volume 1",
        "cantidad": 7,
        "precio": 1200
    },
    {
        "fecha": "2025-04-28",
        "producto": "Smartwatch",
        "cantidad": 8,
        "precio": 150
    },
    {
        "fecha": "2025-05-04",
        "producto": "Berserk Deluxe Volume 1",
        "cantidad": 3,
        "precio": 150
    },
    {
        "fecha": "2025-10-21",
        "producto": "Berserk Deluxe Volume 1",
        "cantidad": 2,
        "precio": 1200
    },
    {
        "fecha": "2025-12-22",
        "producto": "Headphones",
        "cantidad": 7,
        "precio": 600
    },
    {
        "fecha": "2025-07-04",
        "producto": "Tablet",
        "cantidad": 7,
        "precio": 600
    },
    {
        "fecha": "2025-04-26",
        "producto": "teddy cat",
        "cantidad": 6,
        "precio": 1200
    },
    {
        "fecha": "2025-08-12",
        "producto": "teddy",
        "cantidad": 8,
        "precio": 200
    }
]
```

## 2. Ingresos Totales
La lógica de análisis está en el archivo "analizar_core_3.py", primero se cargan los datos de pruebas generados anteriormente.

```
with open('ventas.json', 'r') as archivo:
    ventas = json.load(archivo)
```

Como dice el enunciado de la tarea "Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados". Se inicializa la variable "ingresos_totales" en 0, después se recorre el diccionario calculando el total generado por venta y sumando dicho resultado a la variable de ingresos totales.

```
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]
```

## 3. Producto Más Vendido

Las instrucciones dicen: "Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto". Para implementar lo descrito se define la siguiente función:

```
def get_ventas_por_producto(ventas):
    ventas_por_producto = {}
    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]
        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad
    return ventas_por_producto
```
Esta función simplemente recibe el diccionario de ventas, lo recorre y mientras itera va almacenando en otro diccionario la cantidad acumulada de ventas de cada producto. Utilizando la función se puede obtener el diccionario solicitado de manera simple:
```
ventas_por_producto = get_ventas_por_producto(ventas)
```

Luego se solicita que se identifique el producto más vendido, se debe buscar el máximo en el "ventas_por_producto", se utiliza la función max pero para indicar que este busque en la cantidad y no el nombre del producto se incluye una función anónima lambda.

```
producto_mas_vendido = max(ventas_por_producto, key=lambda producto: ventas_por_producto[producto])
```

## 4. Precio Promedio por Producto

Se define la función "get_precios_por_producto" para crear el diccionario "precios_por_producto", es básicamente la misma lógica, recorrer y almacenar los datos solicitados.


```
def get_precios_por_producto(ventas):
    precios_por_producto = {}
    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]
        if producto in precios_por_producto:
            precios_por_producto[producto] = (precios_por_producto[producto][0] + cantidad*precio, precios_por_producto[producto][1] + cantidad)
        else:
            precios_por_producto[producto] = (cantidad*precio, cantidad)
    return precios_por_producto
```

Se utiliza la función para definir el diccionario solicitado y haciendo uso de este se calcula el promedio de cada producto.

```
precios_por_producto = get_precios_por_producto(ventas)
precio_promedio = {}
for producto, tupla in precios_por_producto.items():
    precio_promedio[producto] = (tupla[0]/tupla[1])
```

## 5. Ingresos Totales por Día

Las instrucciones dicen: "Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día". Para implementar lo descrito se define la siguiente función:

```
def get_ingresos_por_dia(ventas):
    ingresos_por_dia = {}
    for venta in ventas:
        fecha = venta["fecha"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]
        if fecha in ingresos_por_dia:
            ingresos_por_dia[fecha] += cantidad * precio
        else:
            ingresos_por_dia[fecha] = cantidad * precio
    return ingresos_por_dia
```

Esta función simplemente recibe el diccionario de ventas, lo recorre y mientras itera va almacenando en otro diccionario los ingresos acumulados de cada día. Utilizando la función se puede obtener el diccionario solicitado de manera simple:

```
ingresos_por_dia = get_ingresos_por_dia(ventas)
```

## 6. Resumen de Ventas

Las instrucciones dicen: "Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados". Se utiliza la información previamente calculada en las secciones anteriores para construir este resumen:

```
resumen_ventas = {}
for producto in ventas_por_producto:
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": precios_por_producto[producto][0],
        "precio_promedio": precio_promedio[producto]
    }
```

Este diccionario anidado contiene toda la información resumida por producto, combinando la cantidad total vendida, los ingresos totales generados y el precio promedio de venta para cada producto.