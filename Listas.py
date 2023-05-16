# SOLICITAMOS el tamaño de la lista
tamaño = int(input("Ingrese el tamaño de la lista: "))

# Creamos las listas
nombres = []
identificaciones = []

# Pedimos las variables de la lista
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    nombres.append(nombre)
    identificaciones.append(identificación)

# Mostramos los datos de la lista
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])

# Búsqueda en la lista
busqueda = input("Ingrese el nombre a buscar: ")
encontrado = False

for i in range(tamaño):
    if nombres[i] == busqueda:
        print("Nombre:", nombres[i])
        print("Identificación:", identificaciones[i])
        encontrado = True

if not encontrado:
    print("No se encontró ningún nombre coincidente.")