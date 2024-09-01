def cifrado_cesar(texto, rotaciones):
    resultado = ""

    for char in texto:
        # Verificar si el carácter es una letra mayúscula
        if char.isupper():
            resultado += chr((ord(char) - 65 + rotaciones) % 26 + 65)
        # Verificar si el carácter es una letra minúscula
        elif char.islower():
            resultado += chr((ord(char) - 97 + rotaciones) % 26 + 97)
        else:
            # Mantener los caracteres no alfabéticos sin cambios
            resultado += char

    return resultado

# Leer el input del usuario en una sola línea
entrada = input("Ingresar mensaje a cifrar seguido del corrimiento: \n")

# Dividir la entrada en texto y número de rotaciones
texto_plano, numero_rotaciones = entrada.rsplit(' ', 1)
numero_rotaciones = int(numero_rotaciones)

# Cifrar el texto
texto_cifrado = cifrado_cesar(texto_plano, numero_rotaciones)
print("\nMensaje crifrado: \n"+ texto_cifrado +"\n")
