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

SQL = 'SELECT * FROM promedio;'
INSERTAR = 'INSERT INTO promedio (nota1, nota2, nota3, promedio) VALUES (%s, %s, %s, %s)'

print("Ingrese las 3 notas para calcular su promedio")
n1 = int(input("Ingrese su nota 1: "))
n2 = int(input("Ingrese su nota 2: "))
n3 = int(input("Ingrese su nota 3: "))

prom = (n1 + n2 + n3)/3

if prom > 59:
    print("Ha aprobado el curso. Su promedio fue: ", prom)
elif prom < 60:
    print("Ha reprobado el curso. Su promedio fue: ", prom)

cursor = conexion.cursor()

cursor.execute(INSERTAR, (n1, n2, n3, prom))
conexion.commit()
cursor.execute(SQL)

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)