import random
import statistics

## Actividad Numero 1

edad_usuario = float(input("Ingrese su edad: "))

if edad_usuario > 18:
    print("Es mayor de edad")

## Actividad Numero 2

nota = float(input("Ingrese la nota: "))

if nota >= 6:
    print(f"Aprobado")
else:
    print(f"Desaprobado")

## Actividad Numero 3

num = float(input("Ingrese un numero: "))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

## Actividad Numero 4

edad = float(input("Ingrese su edad: "))

if edad < 12:
    print(f"Sos Niño/a")
elif edad >= 12 and edad <= 18:
    print(f"Sos Adolescente")
elif edad >= 18 and edad <= 30:
    print(f"Sos Adulto/a joven")
else:
    print(f"Sos Adulto/a")

## Actividad Numero 5

password = input("Ingresa una contraseña: ")

if len(password) >= 8 and len(password) <= 14:
    print(f"Ha ingresado una contraseña correcta")
else:
    print(f"Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

## Actividad Numero 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana:
    print("Hay sesgo positivo")
elif media < mediana:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")

## Actividad Numero 7

palabra = input("Ingrese una palabra: ")

if palabra[-1] in "aeiou":
    print(palabra + "!")
else:
    print(palabra)

## Actividad Numero 8

nombre = input("Ingrese su nombre: ")
opcion = int(input('1: Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO\n2: Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3: Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n'))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

## Actividad Numero 9

magnitud = float(input("Ingresá la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

## Actividad Numero 10

hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es?: "))

fecha = mes * 100 + dia

if hemisferio == "N":
    if 1221 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Invierno"

elif hemisferio == "S":
    if 1221 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Verano"

else:
    estacion = "Hemisferio inválido"

print(f"La estación del año es: {estacion}")