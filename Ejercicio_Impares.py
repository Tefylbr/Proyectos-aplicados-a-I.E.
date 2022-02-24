import psycopg2

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

SQL = 'SELECT * FROM impares;'
INSERTAR = 'INSERT INTO impares (NImpares, impares) VALUES (%s, %s)'

cont = 0
res = ""

for i in range(1, 100, 2):
    print(i, end=",")
    cont = cont + 1
    r = str(i)
    res = str(res + r)

print("\n")

cursor = conexion.cursor()

cursor.execute(INSERTAR, (cont, res))
conexion.commit()
cursor.execute(SQL)

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)