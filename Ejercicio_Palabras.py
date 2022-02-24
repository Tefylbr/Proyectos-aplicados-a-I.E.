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

SQL = 'SELECT * FROM palabras;'
INSERTAR = 'INSERT INTO palabras VALUES (%s, %s)'


palabra = input("Ingrese una palabra:");
vocales = 0;

for i in palabra:
    vocal = i
    if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal == 'o' or vocal == 'u':
        vocales = vocales + 1

print("La palabra ingresada tiene", vocales, "vocales.")


cursor = conexion.cursor()

cursor.execute(INSERTAR, (palabra, vocales))
conexion.commit()
cursor.execute(SQL)

valores = cursor.fetchall()

cursor.close()
conexion.close()

print(valores)