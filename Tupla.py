#  ingresar el tamaño inicial de la tupla
tamaño_inicial = int(input("Ingrese el tamaño de la tupla: "))
print("-------------------------------------------------------")
# Creamos una lista para almacenar los valores ingresados
valores = []

#  ingresar los valores de la tupla
for i in range(tamaño_inicial):
    valor = input("Ingrese el valor {}: ".format(i + 1))
    valores.append(valor)

# Crea la tupla a partir de la lista de valores
tupla = tuple(valores)
print("-------------------------------------------------------")
# muestra los elementos de la tupla
print("Elementos de la tupla:")
for i, valor in enumerate(tupla, start=1):
    print("Valor {}: {}".format(i, valor))
print("-------------------------------------------------------")
# Información de la tupla
print("Información de la tupla:")
print("Longitud de la tupla:", len(tupla))
print("-------------------------------------------------------")
# Agregar elementos a la tupla
while True:
    agregar = input("¿Desea agregar un valor a la tupla? (s/n): ")
    if agregar.lower() == "s":
        valor_nuevo = input("Ingrese el valor a agregar: ")
        tupla += (valor_nuevo,)
        print("El valor {} ha sido agregado a la tupla.".format(valor_nuevo))
    else:
        break

# Búsqueda de un valor en la tupla
while True:
    print("-------------------------------------------------------")
    buscar = input("¿Desea buscar un valor en la tupla? (s/n): ")
    if buscar.lower() == "s":
        valor_buscar = input("Ingrese el valor a buscar: ")
        if valor_buscar in tupla:
            print("El valor", valor_buscar, "se encuentra en la tupla.")
        else:
            print("El valor", valor_buscar, "no se encuentra en la tupla.")
    else:
        break
print("-------------------------------------------------------")
# Mostrar tupla actualizada
print("Elementos de la tupla:")
for i, valor in enumerate(tupla, start=1):
    print("Valor {}: {}".format(i, valor))

# muestra de la tupla
print("Información de la tupla:")
print("Longitud de la tupla:", len(tupla))
print("-------------------------------------------------------")