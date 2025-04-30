#Actividad N 1

num1_100 = list(range(0,101,4))

#Actividad N 2

mi_lista_favorita = ['Pepsi', 'Coca Cola', 'Sprite', 'Fanta', 'Manaos']
print(mi_lista_favorita[-2])

#Actividad N 3

lista_vacia = []
lista_vacia.append('ahora')
lista_vacia.append('ya')
lista_vacia.append('no')
print(lista_vacia)

#Actividad N 4

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Actividad N 5

numeros = [8,15, 3,22,7] # primero se inicializa la lista numeros
numeros.remove(max(numeros)) # luego con max(numeros) se encuentra al maximo elemento de la lista en este caso 22 y con remove, lo eliminamos
print(numeros) # Imprimos la lista por consola, despues de borrar el elemento.

#Actividad N 6

numeros_5_en_5 = list(range(0,31,5))
print(numeros_5_en_5[0:2])

#Actividad N 7

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["corolla", "etios"]
print(autos)

#Actividad N 8

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Actividad N 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Actividad N 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
