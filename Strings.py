# solicitud de la variable
frase = input("Por favor, introduzca una frase: ")

# longitud de la variable
print("La longitud de la frase es:", len(frase))

# buscador dentro del input
palabra = input("Por favor, introduzca una palabra para buscar en la frase: ")

# Comprueba si la palabra está en la frase
if palabra in frase:
    print("La palabra", palabra, "está en la frase.")
else:
    print("La palabra", palabra, "no está en la frase.")

# Solicita variable para reemplazar en la frase
palabra_a_reemplazar = input("Por favor, introduzca una palabra para reemplazar en la frase: ")
nueva_palabra = input("Por favor, introduzca la nueva palabra: ")

# Reemplaza  y muestra la nueva frase
nueva_frase = frase.replace(palabra_a_reemplazar, nueva_palabra)
print("La nueva frase es:", nueva_frase)