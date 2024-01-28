import string
import random
print("\t---------------------------------------------------------")
print("\tBIENVENIDOS AL GENERADOR DE CONTRASEÑAS SEGURAS DE ALVARO")
print("\t---------------------------------------------------------")
longitud = int(input("\tIngresar Tamaño Que Quieres Que Tenga Tu Contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print(f"\tLa contraseña que se generó es: {contrasena} ")