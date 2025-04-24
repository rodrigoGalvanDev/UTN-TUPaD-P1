import random

#Ejercicio Numero 1

for i in range(101):
    print(i)

#Ejercicio Numero 2

num = int(input("Ingrese un numero entero: "))

contador_digitos = 0

while num > 0:
    num = num // 10
    contador_digitos += 1

print(f"El numero tiene {contador_digitos} digitos")

#Ejercicio Numero 3

num_1 = int(input("Ingrese el primer numero entero: "))
num_2 = int(input("Ingrese el segundo numero entero: "))
suma = 0

for i in range (num_1 + 1, num_2):
    suma += i

print(f"La sumatoria realizada da como resultado: {suma}")

#Ejercicio Numero 4

numero = int(input("Ingrese un numero para ser sumado, si desea detener la operacion ingrese un 0: "))

bandera = True
sumatoria = 0

while bandera:
    if numero != 0:
        sumatoria += numero
        numero = int(input("Ingrese un numero para ser sumado, si desea detener la operacion ingrese un 0: "))
    else:
        print(f"La sumatoria realizada da como resultado: {sumatoria}")
        bandera = False

#Ejercicio Numero 5

num_random = random.randint(0,9)
numero_elegido = int(input("Ingresa un numero entre 0 y 9: "))
flag = True

while flag:
    if numero_elegido == num_random:
        print(f"Ganaste! el numero era {num_random}")
        break
    else:
        numero_elegido = int(input("Buen intento, pero no es el numero. Intentalo de nuevo: "))

#Ejercicio Numero 6

for numero in range(100, -1, -2):
    print(numero)
    

#Ejercicio Numero 7

nume = int(input("Ingrese un numero: "))
sumatoria_2 = 0

for i in range(0, nume + 1):
    sumatoria_2 += i

print(f"La suma entre 0 y {nume} es de: {sumatoria_2}")

#Ejercicio Numero 8

cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingresá el número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#Ejercicio Numero 9

cantidad = 100

suma_total = 0

for i in range(cantidad):
    numero = int(input(f"Ingresá el número {i + 1}: "))
    suma_total += numero

media = suma_total / cantidad

print(f"\nLa media de los {cantidad} números es: {media}")

#Ejercicio Numero 10

numero_int = int(input("Ingresá un número entero: "))

numero_invertido = int(str(abs(numero))[::-1])

# Mostrar resultado, manteniendo el signo si era negativo
if numero_int < 0:
    numero_invertido *= -1

print(f"El número invertido es: {numero_invertido}")
