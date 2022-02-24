import psycopg2

n1 = int(input("Ingrese el número de inicio de la cuenta: "))
n2 = int(input("Ingrese el número de fin de la cuenta: "))

res = ""
for i in range(n1, n2+1, 2):
    print(i)
    r = str(i)
    res = str(res+r)

direccion_conexion = """
    host='localhost' port='5432'user='postgres' password='1234' dbname='ejemploconnpy'
    """
conexion = psycopg2.connect(direccion_conexion)

cursor = conexion.cursor()

# Query
SQL = 'SELECT * FROM de2n2;'
INSERTAR = 'INSERT INTO de2n2 (Numero1, Numero2, Resultado) VALUES (%s, %s, %s)'

cursor.execute(INSERTAR, (n1, n2, res))
conexion.commit()
cursor.execute(SQL)

 # Obtener valores de la base de datos

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)