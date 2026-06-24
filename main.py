import random
import string

# Función para generar la contraseña
def generar_contrasena(longitud, usar_letras, usar_numeros, usar_simbolos):
    caracteres = ""

    if usar_letras == "s":
        caracteres += string.ascii_letters

    if usar_numeros == "s":
        caracteres += string.digits

    if usar_simbolos == "s":
        caracteres += string.punctuation

    if caracteres == "":
        return "Error: debe seleccionar al menos una opción."

    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


# Programa principal
opcion = "s"

while opcion == "s":
    print("\nGENERADOR DE CONTRASEÑAS SEGURAS")

    longitud = int(input("Ingrese la longitud de la contraseña: "))

    usar_letras = input("¿Desea incluir letras? (s/n): ").lower()
    usar_numeros = input("¿Desea incluir números? (s/n): ").lower()
    usar_simbolos = input("¿Desea incluir símbolos? (s/n): ").lower()

    resultado = generar_contrasena(longitud, usar_letras, usar_numeros, usar_simbolos)

    print("\nContraseña generada:")
    print(resultado)

    opcion = input("\n¿Desea generar otra contraseña? (s/n): ").lower()

print("\nGracias por usar el programa.")
