from sys import exit
import sys 
import numpy as np
import os
import psycopg2 

z  = float 
Opcion = "" 
ciclo = 1

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "1234",
        dbname = "ejemploconnpy"
    )
    print("conexion exitosa")
except psycopg2.Error as e:
    print("Ocurrio un error en la conexion")
    print("Verifique los parametros")

SQL = "SELECT * FROM calcu2;"
INSERT = "INSERT INTO calcu2(operacion,primero,segundo,resultado) VALUES (%s, %s,%s,%s);"

while ciclo == 1:
    print("Bienvenido a la calculadora de Pyhton")
    print("Seleccione una opcion")
    print("Suma.......................................(s)")
    print("Resta......................................(r)")
    print("Multiplicacion.............................(m)")
    print("Division...................................(d)")
    print("Exponencial................................(e)")
    print("Raiz ......................................(rc)")
    print("Ver historial de base de datos.............(h)")
    print("Salir......................................(o)")


    Opcion = str(input())
    try: 
        if Opcion == "s": 
            print("Opcion seleccionada fue suma")
            operacion ="suma"
            x =  int(input("Ingrese el primer numero "))  
            y =  int(input("Ingrese el segundo numero "))
            z = x + y
            print("Resultado de la suma es:", z)
            try: 
                cursor = conexion.cursor()
                cursor.execute (INSERT, (operacion, x, y, z))
                conexion.commit()
            except: 
                print("Datos ingresados incorrectos")
        elif Opcion == "r":
            operacion ="resta"
            print("Opcion seleccionada fue resta")
            x =  int(input("Ingrese el primer numero "))
            y =  int(input("Ingrese el segundo numero "))
            z = x - y
            print("Resultado de la resta es:", z)
            try: 
                cursor = conexion.cursor()
                cursor.execute (INSERT, (operacion, x, y, z))
                conexion.commit()
            except: 
                print("Datos ingresados incorrectos")
        elif Opcion == "m":
            operacion ="multiplicacion"
            print("Opcion seleccionada fue multiplicacion")
            x =  int(input("Ingrese el primer numero "))
            y =  int(input("Ingrese el segundo numero "))
            z = x * y
            print("Resultado de la multiplicacion es:", z)
            try: 
                cursor = conexion.cursor()
                cursor.execute (INSERT, (operacion, x, y, z))
                conexion.commit()
            except: 
                print("Datos ingresados incorrectos")
        elif Opcion == "d":
            operacion = "division"
            print("Opcion seleccionada fue division")
            x = int(input("Ingrese el primer numero "))
            y = int(input("Ingrese el segundo numero "))
            if (y != 0):
                z = x / y
                print("Resultado de la division es:", z)
                try: 
                    cursor = conexion.cursor()
                    cursor.execute (INSERT, (operacion, x, y, z))
                    conexion.commit()
                except: 
                    print("Datos ingresados incorrectos")
            elif (y==0):
                print("Resultado de la division entre cero no es posible")
        elif Opcion == "e":
            operacion = "exponencial"
            print("Opcion seleccionada fue exponencial")
            x = int(input("Ingrese el numero base "))
            y = int(input("Ingrese el exponente "))
            z = (np.power(x,y)) 
            print("Resultado de la operacion es:", z)
            try: 
                cursor = conexion.cursor()
                cursor.execute (INSERT, (operacion, x, y, z))
                conexion.commit()
            except: 
                print("Datos ingresados incorrectos")
        elif Opcion == "rc":
            operacion ="raiz n"
            print("Opcion seleccionada fue raiz")
            x = int(input("Ingrese el numero "))
            y = int(input("Ingrese el valor de la raiz que desea obtener "))
            z = (np.power(x,(1/y))) 
            print("Resultado de la raiz es:", z)
            try: 
                cursor = conexion.cursor()
                cursor.execute (INSERT, (operacion, x, y, z))
                conexion.commit()
            except: 
                print("Datos ingresados incorrectos")
        elif Opcion == "h":
                cursor = conexion.cursor()
                cursor. execute(SQL)
                valores = cursor.fetchall()
                cursor.close()
                conexion.close()
                print(valores)
        elif Opcion == "o":
                ciclo=0
                print("Gracias por utilizar nuestra plataforma")
                print("Sthephanie Lorena Bonilla Rodriguez 201900300")
    except: 
        if not type(x, y) is int:
            raise TypeError("Solo numeros aceptados")
        if Opcion != "o": 
            print("Pulse cualquier tecla para regresar al menu")
            Opcion = str(input())
