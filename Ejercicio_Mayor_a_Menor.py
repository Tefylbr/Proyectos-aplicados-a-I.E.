import psycopg2
ciclo=1 
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

SQL = 'SELECT * FROM mayormenor;'
INSERTAR = 'INSERT INTO mayormenor (Numero1, Numero2, Mayor_menor) VALUES (%s, %s, %s)'

n1 = int(input("Ingrese el primer número "))
n2 = int(input("Ingrese el segundo número: "))
res = ""
if n1 > n2:
    for i in range(n1, n2, -1):
        print(i, end=",")
        r = str(i)
        res = str(res + r)
elif n2 > n1:
    for i in range(n2, n1, -1):
        print(i, end=",")
        r = str(i)
        res = str(res + r)

cursor = conexion.cursor()
cursor.execute(INSERTAR, (n1, n2, res))
conexion.commit()
cursor.execute(SQL)
valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)