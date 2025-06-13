import math

# Ejercicio Numero 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# Ejercicio Numero 2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario("Sebastian")

# Ejercicio Numero 3

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")

informacion_personal("Andrea", "Diaz", 23, "Cordoba")

# Ejercicio Numero 4

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El area del circulo es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * radio * math.pi
    print(f"El perimetro del circulo es de: {perimetro}")

calcular_area_circulo(float(input("Ingresa el radio para calcular el area del circulo: ")))
calcular_perimetro_circulo(float(input("Ingresa el radio para calcular el perimetro del circulo: ")))

# Ejercicio Numero 5

def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos equivale a {horas} horas")

segundos_a_horas(float(input("Ingresa los segundos para convertirlos a horas: ")))

# Ejercicio Numero 6

def tabla_multiplicar(numero):
    print(f"{numero} x 1 = {numero * 1}\n{numero} x 2 = {numero * 2}\n{numero} x 3 = {numero * 3}\n{numero} x 4 = {numero * 4}\n{numero} x 5 = {numero * 5}\n{numero} x 6 = {numero * 6}\n{numero} x 7 = {numero * 7}\n{numero} x 8 = {numero * 8}\n{numero} x 9 = {numero * 9}\n{numero} x 10 = {numero * 10}\n")


tabla_multiplicar(int(input("Ingresa un numero para mostrarte la tabla de multiplicar: ")))

# Ejercicio Numero 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "División por cero no permitida"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingresa el primer numero para realizar las operaciones basicas: "))
b = float(input("Ingresa el segundo numero para realizar las operaciones basicas: "))
resultado = operaciones_basicas(a, b)

print(f"Suma entre {a} y {b}: {resultado[0]}")
print(f"Resta entre {a} y {b}: {resultado[1]}")
print(f"Multiplicación entre {a} y {b}: {resultado[2]}")
print(f"División entre {a} y {b}: {resultado[3]}")

# Ejercicio Numero 8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Su IMC es: {imc:.2f}")

calcular_imc(float(input("Ingresa tu peso en kg: ")),float(input("Ingresa tu altura en metros: ")))

# Ejercicio Numero 9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados celcius equivale a {fahrenheit:.2f} grados fahrenheit")

celsius_a_fahrenheit(float(input("Ingresa la temperatura en celcius para ser convertida: ")))

# Ejercicio Numero 10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio entre {a},{b} y {c} es de: {promedio:2f}")

calcular_promedio(float(input("Ingresa el primer numero para calcular su promedio: ")),float(input("Ingresa el segundo numero para calcular su promedio: ")),float(input("Ingresa el tercer numero para calcular su promedio: ")))
