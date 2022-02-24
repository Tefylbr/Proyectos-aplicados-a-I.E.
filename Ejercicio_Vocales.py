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

SQL = 'SELECT * FROM vocales;'
INSERTAR = 'INSERT INTO vocales (palabra, A, E, I, O, U) VALUES (%s, %s, %s, %s, %s, %s)'

palabra = input("Ingrese una palabra:")
A = E = I = O = U = 0
palabra = palabra.upper().strip()

for i in palabra:
    if i == 'A':
        A = A + 1
    if i == 'E':
        E = E + 1
    if i == 'I':
        I = I + 1
    if i == 'O':
        O = O + 1
    if i == 'U':
        U = U + 1

print("La palabra", palabra, "contiene: \n A= ", A, "\n E= ", E, "\n I= ", I, "\n O= ", O, "\n U= ", U)

cursor = conexion.cursor()

cursor.execute(INSERTAR, (palabra, A, E, I, O, U))
conexion.commit()
cursor.execute(SQL)

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)
