import mysql.connector

# Establece la conexión con la base de datos MySQL
mydb = mysql.connector.connect(
  host="local_host",
  user="root",
  password="AxENM8013txt*rO",
  database="mysql"
)

# Crea un objeto cursor para ejecutar consultas SQL
mycursor = mydb.cursor()

# Ejecuta una consulta SQL
mycursor.execute("SELECT * FROM tu_tabla")

# Obtiene los resultados de la consulta
resultados = mycursor.fetchall()

# Muestra los resultados
for resultado in resultados:
  print(resultado)
