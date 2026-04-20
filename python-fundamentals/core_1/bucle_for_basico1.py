
# 1. Básico: imprime todos los números enteros del 0 al 100.

print("Básico: imprime todos los números enteros del 0 al 100.")
for i in range(101):
    print(i)

# 2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500

print("\nMúltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500")
for i in range(2,501,2):
    print(i)

# 3. Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es 
# divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10,
# imprime “baby”
#Nota: no entendí bien la consigna, así que hice dos interpretaciones distintas.

# Opción 1: interpretación donde si un número es divisible por 10, 
# se imprime "baby" y  "ice ice", porque también es divisible por 5. 
# for i in range(1,101):
#     if i % 10 == 0:
#         print("ice ice baby")
#     elif i % 5 == 0:
#         print("ice ice")
#     else:
#         print(i)

# Opción 2: interpretación donde si un número es divisible por 10, 
# se imprime "baby" y no se imprime "ice ice", porque el número ya fue 
# clasificado como múltiplo de 10.

print("\nContando Vanilla Ice")
for i in range(1,101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)


# 4. Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime
#  la suma total. (Sorpresa, será un número gigante).
# n(n + 1) es la fórmula para sumar los primeros n números enteros. 
# 250000(250000 + 1) = 250000 * 250001 = 62500250000.

print("\nWow. Número gigante a la vista")
total = 0
for i in range(2,500001,2):
    total += i
print(total)

# 5.Regrésame al 3: imprime los números positivos comenzando desde 2024, 
# en cuenta regresiva de 3 en 3.
# Nota: no lo regresa al 3, deberia empezar en 2025 o un multiplo de 3
# para que el último número sea 3.

print("\nRegrésame al 3")
for i in range(2024, 0, -3):
    print(i)

# 6. Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. 
# Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean
#  múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, 
# el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

print("\nContador dinámico")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
