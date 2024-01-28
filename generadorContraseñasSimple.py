import string
import random

while True:
    print("\t---------------------------------------------------------")
    print("\tBIENVENIDOS AL GENERADOR DE CONTRASEÑAS SEGURAS DE ALVARO")
    print("\t---------------------------------------------------------")


    longitud = int(input("\tIngresar Tamaño Que Quieres Que Tenga Tu Contraseña: "))

    if longitud <= 0:
        print("\tLa longitud de la contraseña debe ser mayor que cero. Inténtalo de nuevo.")
        continue

    caracteres = string.ascii_letters + string.digits + string.punctuation

    contrasena = "".join(random.choice(caracteres) for i in range(longitud))

    print(f"\tLa contraseña que se generó es: {contrasena} ")
    print("\t")
    salir = input("\t¿Quieres salir? Presiona la letra 'S' para salir, o cualquier otra tecla para generar otra contraseña: ")
    if salir.upper() == 'S':
        break
