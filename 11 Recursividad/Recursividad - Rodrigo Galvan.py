#Ejercicio Numero 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Ingresa un numero para saber su factorial: "))

for i in range(1,num+1):
    print(factorial(i))

#Ejercicio Numero 2

def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1                
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

num = int(input("Ingresa un numero: "))

for i in range(0,num):
    print(fibonacci_recursivo(i))


#Ejercicio Numero 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero >= 0): "))

resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es {resultado}")

#Ejercicio Numero 4

def decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))

if numero == 0:
    print("0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

# Ejercicio Numero 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra sin espacios ni tildes: ").lower()
print(es_palindromo(texto))

# Ejercicio Numero 6

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234))  # 10
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8

#Ejercicio Numero 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(1))  # 1
print(contar_bloques(2))  # 3
print(contar_bloques(4))  # 10

# Ejercicio Numero 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        contador_actual = 1 if (numero % 10) == digito else 0
        return contador_actual + contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2))  # 3
print(contar_digito(5555, 5))      # 4
print(contar_digito(123456, 7))    # 0
