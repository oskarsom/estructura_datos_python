# introducir valores para el conjunto A
conjunto_a = set()
num_elementos_a = int(input("Introduzca el número de elementos en el conjunto A: "))
for i in range(num_elementos_a):
    elemento = input("Introduzca el elemento " + str(i + 1) + " del conjunto A: ")
    conjunto_a.add(elemento)

# introducir valores para el conjunto B
conjunto_b = set()
num_elementos_b = int(input("Introduzca el número de elementos en el conjunto B: "))
for i in range(num_elementos_b):
    elemento = input("Introduzca el elemento " + str(i + 1) + " del conjunto B: ")
    conjunto_b.add(elemento)

#  imprime la unión de los conjuntos A y B
union = conjunto_a.union(conjunto_b)
print("La unión de los conjuntos A y B es:", union)

# imprime la intersección de los conjuntos
interseccion = conjunto_a.intersection(conjunto_b)
print("La intersección de los conjuntos A y B es:", interseccion)

# imprime la diferencia de A y B
diferencia = conjunto_a.difference(conjunto_b)
print("La diferencia entre los conjuntos A y B es:", diferencia)