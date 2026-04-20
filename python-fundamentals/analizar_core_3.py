import json

############################################################
# Funciones
############################################################

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



def get_ingresos_por_dia(ventas):
    ingresos_por_dia = {}
    for venta in ventas:
        fecha = venta["fecha"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]
        if fecha in ingresos_por_dia:
            ingresos_por_dia[fecha] += cantidad*precio
        else:
            ingresos_por_dia[fecha] = cantidad*precio
    return ingresos_por_dia



def get_resumen_ventas(precios_por_producto):
    resumen_ventas = {}
    for producto, cantidad in precios_por_producto.items():
        resumen_ventas[producto] = {
            "cantidad_total": cantidad[1],
            "ingresos_totales": cantidad[0],
            "precio_promedio": cantidad[0] / cantidad[1] if cantidad[1] > 0 else 0
        }
    return resumen_ventas

# 1.- Carga de datos
with open('ventas.json', 'r') as archivo:
    ventas = json.load(archivo)


# 2. Cálculo de Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]


# 3. Análisis del Producto Más Vendido
ventas_por_producto = get_ventas_por_producto(ventas)
producto_mas_vendido = max(ventas_por_producto, key=lambda producto: ventas_por_producto[producto])
# print(f"producto mas vendido: {producto_mas_vendido}")

# 4. Promedio de Precio por Producto:
precios_por_producto = get_precios_por_producto(ventas)
precio_promedio = {}
for producto, tupla in precios_por_producto.items():
    precio_promedio[producto] = (tupla[0]/tupla[1])


# 5. Ventas por Día
ingresos_por_dia = get_ingresos_por_dia(ventas)


# 6. Representación de Datos
resumen_ventas = get_resumen_ventas(precios_por_producto)
# print(json.dumps(resumen_ventas, indent=4, ensure_ascii=False))