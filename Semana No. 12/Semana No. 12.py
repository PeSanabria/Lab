print("Semana 12: Ejercicio 1")
print("a. Sumatoria")
print("b. Factorial")
print("c. Tablas de multiplicar")
print("d. Numero Perfecto")
opcion=input("Elija una opcion a calcular: ")

match(opcion):
    case "a":
        N=0
        while N<=0:
           N=int(input("Ingrese un numero entero positivo: "))
        if N<=0:
            print("El numero ingresado debe ser entero positivo.")
        sumatoria=0
        for cont in range(1,N+1):
            sumatoria+=cont 
        print("La sumatoria es:",sumatoria)
    case "b":
        N=0
        while N<=0:
            N=int(input("Ingrese un numero entero positivo: "))
            if N<=0:
                print("El numero ingresado debe ser entero positivo.")
        factorial=1
        for cont in range(1,N+1):
            factorial*=cont
        for i in range (1,11):
            for j in range(1,11):
                print(i*j,"/t",end='')
                print()
    case "d":
        N=0
        while N<=0:
            N=int(input("Ingrese un numero entero positivo: "))
            if N<=0:
                print("El numero ingresado debe ser entero positivo.")
        acumulado=0
        for factori in range(1,N):
            if N%factori==0:
                acumulado+=factori
            if N== acumulado:
                print("es perfecto")
            else:
                print("no es perfecto")
    case _:
        print("Elija una opcion valida")
