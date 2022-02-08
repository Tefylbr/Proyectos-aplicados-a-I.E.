from sys import exit 
import numpy as np
import os

z = float
Opcion = "" 
ciclo = 1

while ciclo == 1:
    print("Bienvenido a la calculadora de Pyhton")
    print("Seleccione una opcion")
    print("Opcion Suma..............(s)")
    print("Opcion Resta.............(r)")
    print("Opcion Multiplicacion........(m)")
    print("Opcion Division...........(d)")
    print("Opcion Exponencial...........(e)")
    print("Opcion raiz cuadrada...........(rc)")
    print("Opcion Salir.............(o)")

    Opcion = str(input())
    try:
        if Opcion == "s": 
            print("Opcion seleccionada fue suma")
            x = int(input("Ingrese el primer numero"))
            y = int(input("Ingrese el segundo numero"))
            z = x + y
            print("Resultado de la suma es:", z)
        elif Opcion == "r":
            print("Opcion seleccionada fue resta")
            x = int(input("Ingrese el primer numero"))
            y = int(input("Ingrese el segundo numero"))
            z = x - y
            print("Resultado de la resta es:", z)
        elif Opcion == "m":
            print("Opcion seleccionada fue multiplicacion")
            x = int(input("Ingrese el primer numero"))
            y = int(input("Ingrese el segundo numero"))
            z = x * y
            print("Resultado de la multiplicacion es:", z)
        elif Opcion == "d":
            print("Opcion seleccionada fue division")
            x = int(input("Ingrese el primer numero"))
            y = int(input("Ingrese el segundo numero"))
            if (y != 0):
                z = x / y
                print("Resultado de la division es:", z)
            elif (y==0):
                print("Resultado de la division entre cero no es posible")
        elif Opcion == "e":
            print("Opcion seleccionada fue exponencial")
            x = int(input("Ingrese el numero base"))
            y = int(input("Ingrese el exponente"))
            z = (np.power(x,y)) 
            print("Resultado de la operacion es:", z)
        elif Opcion == "rc":
            print("Opcion seleccionada fue raiz cuadrada")
            x = int(input("Ingrese el numero"))
            y = int(input("Ingrese el valor de la raiz que desea obtener"))
            z = (np.power(x,(1/y))) 
            print("Resultado de la raiz cuadrada es:", z)
        elif Opcion == "o":
            ciclo=0
            print("Gracias por utilizar nuestra plataforma")
            print("Sthephanie Lorena Bonilla Rodriguez 201900300")
            exit()
    except: 
        if not type(x, y) is int:
            raise TypeError("Solo numeros aceptados")
        if Opcion != "o": 
            print("Pulse cualquier tecla para regresar al menu")
            Opcion = str(input())
