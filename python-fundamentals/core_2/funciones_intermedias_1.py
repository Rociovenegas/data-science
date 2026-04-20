############################################################
# 1. Actualizar valores en diccionarios y listas
############################################################

matriz = [ [10, 15, 20], [3, 7, 14] ]
# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: 
# [ [10, 15, 20], [6, 7, 14] ]

matriz[1][0] = 6
print(matriz)

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"
# cantantes[0].update({"nombre": "Enrique Martin Morales"})
print(cantantes)

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

# Cambia “Cancún” por “Monterrey” en la lista de ciudades de México.
ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# En las coordenadas, cambia el valor de “latitud” por 9.9355431

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

############################################################
# 2. Iterar a través de una lista de diccionarios
############################################################


# Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada 
# diccionario de la lista e imprima cada llave y el valor correspondiente.

def iterarDiccionario(lista):
    for cantante in lista:
        partes = []
        for clave, valor in cantante.items():
            partes.append(f"{clave} - {valor}")
        print(", ".join(partes))

cantantes2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes2)

############################################################
# 3. Obtener valores de una lista de diccionarios
############################################################

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
        else:
            print(f"La llave '{llave}' no se encuentra en el diccionario: {diccionario}")
    
iterarDiccionario2("nombre", cantantes2)
iterarDiccionario2("pais", cantantes2)


############################################################
# 4. Iterar a través de un diccionario con valores de lista
############################################################


def imprimirInformacion(diccionario):
    for lista in diccionario:
        print(f"{len(diccionario[lista])} {lista.upper()}")
        for elemento in diccionario[lista]:
            print(elemento)
        print()

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)