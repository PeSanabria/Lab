import math

print("Semana No. 12: Ejercicio 1")

def obtener_area_triangulo(base, altura):
    return (base * altura) / 2

def obtener_area_cuadrado(lado):
    return lado * lado

def obtener_area_rectangulo(base, altura):
    return base * altura

def obtener_area_circulo(radio):
    return math.pi * (radio ** 2)


opcion = input("""Seleccione la opción que desea calcular:
a. Área de triángulo
b. Área de cuadrado
c. Área de rectángulo
d. Área de círculo
Opción: """)

if opcion == 'a':
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = obtener_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area}")
elif opcion == 'b':
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = obtener_area_cuadrado(lado)
    print(f"El área del cuadrado es: {area}")
elif opcion == 'c':
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = obtener_area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area}")
elif opcion == 'd':
    radio = float(input("Ingrese el radio del círculo: "))
    area = obtener_area_circulo(radio)
    print(f"El área del círculo es: {area}")
else:
    print("Opción no válida")



coordenada_X = 0
coordenada_Y = 0

print("Semana No. 12: Ejercicio 2")


def mover_hacia_arriba():
    global coordenada_Y
    coordenada_Y += 1

def mover_hacia_abajo():
    global coordenada_Y
    coordenada_Y -= 1

def mover_hacia_la_derecha():
    global coordenada_X
    coordenada_X += 1

def mover_hacia_la_izquierda():
    global coordenada_X
    coordenada_X -= 1

print("Semana No. 12: Ejercicio 2")

while True:
    opcion = input("""Seleccione una opción:
a. Sube
b. Baja
c. Izquierda
d. Derecha
e. Salir
Opción: """)

    if opcion == 'a':
        mover_hacia_arriba()
    elif opcion == 'b':
        mover_hacia_abajo()
    elif opcion == 'c':
        mover_hacia_la_izquierda()
    elif opcion == 'd':
        mover_hacia_la_derecha()
    elif opcion == 'e':
        break
    else:
        print("Opción no válida")

print(f"Coordenadas finales del personaje: {coordenada_X}, {coordenada_Y}")
