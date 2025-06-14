#Ejercicio Numero 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

#Ejercicio Numero 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

#Ejercicio Numero 3

lista_frutas = precios_frutas.keys()
print(lista_frutas)

#Ejercicio Numero 4

contactos = {}
contador = 0
while contador < 5:
    contactos[input('Ahora ingrese su nombre: ')] = int(input("Ingrese el numero a agendar: "))
    contador += 1

contacto_buscar = contactos.get(input('Ingresa el nombre del contacto para saber su numero: '))
if contacto_buscar:
    print(f"El numero del contacto ingresado es: {contacto_buscar}")
else:
    print("El contacto no existe.")

#Ejercicio Numero 5

frase = input("Ingresa una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

print(palabras_unicas)

frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("Frecuencia de palabras:", frecuencia_palabras)

#Ejercicio Numero 6

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    notas = input(f"Ingresá 3 notas separadas por espacios para {nombre}: ")
    tupla_notas = tuple(map(float, notas.split()))
    alumnos[nombre] = tupla_notas

print("\nPromedios de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Ejercicio Numero 7

parcial1 = {"Ana", "Juan", "Luis", "Carla"}
parcial2 = {"Luis", "Carla", "Marta", "Pedro"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#Ejercicio Numero 8

stock = {
    "manzanas": 10,
    "bananas": 5,
    "peras": 8
}

producto = input("Ingresá el nombre del producto que querés consultar: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    
    agregar = input(f"¿Querés agregar unidades a {producto}? (sí/no): ").lower()
    if agregar == "sí":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    print(f"{producto} no está en el inventario.")
    agregar_nuevo = input("¿Querés agregarlo como nuevo producto? (sí/no): ").lower()
    if agregar_nuevo == "sí":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] = unidades
        print(f"{producto} agregado al inventario con {unidades} unidades.")

print("\nInventario actualizado:")
for prod, cant in stock.items():
    print(f"{prod}: {cant}")

#Ejercicio Numero 9

agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "14:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"A las {hora} del {dia} tenés: {agenda[clave]}")
else:
    print("No hay eventos programados para ese día y hora.")

#Ejercicio Numero 10

paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Brasil": "Brasilia",
    "Japón": "Tokio"
}

capitales_a_paises = {}

for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

print("Diccionario invertido (capital -> país):")
print(capitales_a_paises)

