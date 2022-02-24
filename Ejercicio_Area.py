import math
import psycopg2

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
except psycopg2.Error as e:
    print("Ocurrio un error en la conexion")
    print("Verifique los parametros")

SQL = "SELECT * FROM areas;"
INSERTAR = "INSERT INTO areas(figura, area) VALUES (%s, %s);"

while ciclo == 1:
    
    Opcion=str(input())
    try: 
            
        print("Escoja l área de qué figura desea calcular ")
        print("Circulo")
        print("Triangulo")
        print("Cuadrado")
        print("Rectangulo")
        print("Seleccione h para ver el historial de calculos")
        fig=str(input(""))
       
        if fig == "Circulo":
            r = float(input("Ingrese el radio del círculo: "))
            area = math.pi*r*r
            print("El área es: ", area)       
            cursor = conexion.cursor()    
            cursor.execute(INSERTAR, (fig, area))
            conexion.commit()
            
        elif fig == "Triangulo":
            b = float(input("Ingrese la medida de la base del triángulo: "))
            a = float(input("Ingrese la medida de la altura del triángulo: "))
            area = (b*a)/2            
            print("El área del triángulo es: ", area)
            cursor = conexion.cursor()
            cursor.execute(INSERTAR, (fig, area))
            conexion.commit()
            
        elif fig == "Cuadrado":
            arista = float(input("Ingrese la medida de la arista del cuadrado: "))
            area = arista*arista
            print("El área del cuadrado es: ", area)
            cursor = conexion.cursor()
            cursor.execute(INSERTAR, (fig, area))
            conexion.commit()
            
        elif fig == "Rectangulo":
            b = float(input("Ingrese la medida de la base del rectangulo: "))
            a = float(input("Ingrese la medida de la altura del rectangulo: "))
            area = b * a
            print("El área del rectanguloo es: ", area)
            cursor = conexion.cursor()
            cursor.execute(INSERTAR, (fig, area))
            conexion.commit()
            
        elif fig == "h":
            cursor = conexion.cursor()
            cursor.execute(SQL)
            valores = cursor.fetchall()    
            print(valores) 
            cursor.close()
            conexion.close()
        elif fig=="z":
            cursor.close()
            conexion.close()
            ciclo=0
              
        else:
            print("No ha seleccionado una de las figuras disponibles.")    
    except: 
        if not type(fig, area) is int:
            raise TypeError("Solo numeros aceptados")
        if Opcion != "o": 
            print("Pulse cualquier tecla para regresar al menu")
            Opcion = str(input())

        
