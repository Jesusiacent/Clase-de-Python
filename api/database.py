import sqlite3

conn = sqlite3.connect('datos.db') #coneccion a la base de datos (se creara si no existe)

#crea un cursor para interactuar con la base de datos
cursor = conn.cursor()

#crear una tabla llamada usuarios con tres columnos: id, nombre y edad
cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               nombre TEXT NOT NULL,
                edad INTEGER
               )''')

#guardar los cambios y cerrar la conexion
conn.commit()
conn.close()

conn = sqlite3.connect('datos.db')

cursor = conn.cursor()

cursor.execute('INSERT INTO usuario (nombre, edad) VALUES (?, ?)', ("Jesus", 36))

conn.commit()
conn.close()
