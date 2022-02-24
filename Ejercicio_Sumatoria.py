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

SQL = 'SELECT * FROM suma;'
INSERTAR = 'INSERT INTO suma (numero, Rsuma) VALUES (%s, %s)'

n = int(input("Ingrese un numero: "))
sumatoria = 0

for i in range(0, n+1, 1):
    sumatoria = sumatoria + i

cursor = conexion.cursor()

cursor.execute(INSERTAR, (n, sumatoria))
conexion.commit()
cursor.execute(SQL)

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)