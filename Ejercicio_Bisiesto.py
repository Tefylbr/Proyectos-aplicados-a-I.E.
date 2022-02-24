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

SQL = 'SELECT * FROM bisiesto;'
INSERTAR = 'INSERT INTO bisiesto (anio, Bisiesto) VALUES (%s, %s)'

ano = int(input("Ingrese su año de nacimiento: "))

if ano % 4 == 0:
    print("El año es bisiesto.")
    Tipo = "Bisiesto"
else:
    print("El año no es bisiesto.")
    Tipo = "No Bisiesto"

cursor = conexion.cursor()

cursor.execute(INSERTAR, (ano, Tipo))
conexion.commit()
cursor.execute(SQL)

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)