import psycopg2

n1 = int(input("Ingrese un número cualquiera: "))
n2 = int(input("Ingrese un número cualquiera: "))
n3 = int(input("Ingrese un número cualquiera: "))

if n1 > n2 and n1 > n3:
    res = n1+n2+n3
    print(n1+n2+n3)
elif n2 > n1 and n2 > n3:
    res = n1*n2*n3
    print(n1*n2*n3)
elif n3 > n1 and n3 > n2:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(str(n1+n2+n3))
    res = int(n1+n2+n3)
elif n3 == n2 == n1:
    print("Todos son iguales: ", n1, n2, n3)
if n2 == n1 and n3 != n1:
    print("Numero disinto es:", n3)
    res = n3
elif n2 == n3 and n1 != n2:
    print("Numero distinto es:", n1)
    res = n1
if n1 == n3 and n2 != n1:
    print("Numero distinto es:", n2)
    res = n2

direccion_conexion = """
    host='localhost' port='5433'user='postgres' password='Ignyte1234' dbname='postgres'
    """
conexion = psycopg2.connect(direccion_conexion)

cursor = conexion.cursor()

# Query
SQL = 'SELECT * FROM ejercicio_numeros;'
INSERTAR = 'INSERT INTO ejercicio_numeros (n1, n2, n3, res) VALUES (%s, %s, %s, %s)'

cursor.execute(INSERTAR, (n1, n2, n3, res))
conexion.commit()
cursor.execute(SQL)

 # Obtener valores de la base de datos

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)