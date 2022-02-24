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

    

# Query
SQL = 'SELECT * FROM divisores2;'
INSERTAR = 'INSERT INTO divisores2 (numero, divisores) VALUES (%s, %s)'

while ciclo == 1:
    n1 = int(input("Ingrese el numero deseado:"))
    for i in range(1, n1 + 1):
        residuo = n1 / i
        if residuo == int(residuo):
            print("Los divisores del numero", n1, "son:", i)
            cursor = conexion.cursor()
            cursor.execute(INSERTAR, (n1, i))
            conexion.commit()
    if n1 == "z":
        ciclo == 0

# Obtener valores de la base de datos
cursor.execute(SQL)
valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)
