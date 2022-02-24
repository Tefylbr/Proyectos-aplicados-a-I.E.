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

SQL = 'SELECT * FROM triangulos;'
INSERTAR = 'INSERT INTO triangulos(lado1, lado2, lado3, tipo) VALUES (%s, %s, %s, %s)'

l1 = int(input("Ingrese el primer lado "))
l2 = int(input("Ingrese el segundo lado: "))
l3 = int(input("Ingrese el tercer lado: "))

if l3 == l2 == l2:
    print("El triangulo es equilatero.")
    tipo = "Equilatero"
elif (l3 == l2) or (l3 == l1) or (l1 == l2):
    print("El triangulo es Isosceles.")
    tipo = "Isosceles"
else:
    print("El triangulo es Escaleno.")
    tipo = "Escaleno"

cursor = conexion.cursor()

cursor.execute(INSERTAR, (l1, l2, l3, tipo))
conexion.commit()
cursor.execute(SQL)

 # Obtener valores de la base de datos

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)