import random

print("Semana No. 16: Ejercicio 1")

lista =  [ ]

for x in range(10):
    lista.append(random.randint(0,10))

    opcion = 'a'

    while(opcion != 'e'):
        print("Menú")
        print("a. Mostrar números", "b. Promedio", "c. Longitud", "d. Suma posiciones impares y pares")
        opcion = input("ingrese su opción: ")

        match opcion:
            case 'a':
                for x in range (len(lista)):
                    print(f"No. {x}: {lista[x]}")
            case 'b':
                print ("Pomedio")
                suma=0
                for x in range (len(lista)):
                    suma+= lista[x]
                promedio = suma / len(lista)
                print (f"----Promedio: {promedio}")

            case 'c':
                print ("Longitud")
                for x in range (len(lista)):
                    print(len[lista])

            case 'd':
                sumapar = 0
                sumaimpar = 0
                print("Suma pares e impares")
                for x in range (len(lista)):
                    if(len(lista)% 2 == 0):
                        sumapar+= lista [x]
                    else:
                         sumaimpar+= lista [x]

                print(f"Suma pares: {sumapar}")
                print(f"Suma impares: {sumaimpar}")



print("Semana No. 16: Ejercicio 2")

cantFilas = int(input("Ingrese cantidad de filas: "))
cantCols = int(input("Ingrese cantidad de columnas: "))

matriz = [[0 for x in range(cantCols)] for y in range(cantFilas)]
mayor = 0
menor = 1000  
pares = 0
impares = 0

for xFilas in range(cantFilas):
    for xCols in range(cantCols):
        matriz[xFilas][xCols] = random.randint(0, 1000)

        
        if matriz[xFilas][xCols] % 2 == 0:
            pares += 1
        else:
            impares += 1

        
        if matriz[xFilas][xCols] > mayor:
            mayor = matriz[xFilas][xCols]
        if matriz[xFilas][xCols] < menor:
            menor = matriz[xFilas][xCols]

print("Matriz:")
for fila in matriz:
    print(fila)

print(f"\nCantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")
