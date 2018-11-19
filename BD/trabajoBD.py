import sqlite3
import timeit

#comenzamos a medir el tiempo
inicio = timeit.default_timer()

# Creamos la BD dentro de la carpeta 'data' 
conexion = sqlite3.connect('./data/adm_cursos.db')
# Obtenemos el cursor del modulo de conexion.
cursor = conexion.cursor()

# SQL para la creacion de la tabla
sql_crear_persona = """CREATE TABLE IF NOT EXISTS Persona (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        nombre varchar(45),
                        apellido varchar(45)
                    ); """
# ejecutamos la creacion de la tabla
cursor.execute(sql_crear_persona)

# --- Insert ---
# creamos lista de 5 personas
personas = [
    (1, "Ismael", "Teixeira"), 
    (2, "Yonder", "Rosales"), 
    (3, "Luis", "Valladares"), 
    (4, "Marvian", "Montoya"),
    (5, "Maria", "Arriaga") 
]
# creamos SQL para la insercion
sqlPersonas = """ INSERT INTO Persona (id, nombre, apellido) VALUES (?,?,?) """
# ejecutamos
cursor.executemany(sqlPersonas, personas)
# hacemos commit para guardar los cambios en la BD
conexion.commit()
# --- Insert ---

# --- Update ---
# creamos SQL para update
sql = ''' UPDATE Persona SET nombre = ?, apellido = ? WHERE id = ? '''
# ejecutamos
cursor.execute(sql, ['Ismaelito', 'Teixeirinha', 1])
# hacemos commit para guardar los cambios en la BD
conexion.commit()
# --- Update ---

# --- Delete ---
# creamos SQL para delete
sql = ''' DELETE FROM Persona WHERE id = 3 '''
# ejecutamos
cursor.execute(sql)
# hacemos commit para guardar los cambios en la BD
conexion.commit()
# --- Delete ---

# --- Read ---
# creamos SQL para read
sql = """ SELECT * FROM Persona """
# ejecutamos
cursor.execute(sql)
# obtenemos todos los valores de la consulta
personas = cursor.fetchall()
#pasamos a imprimir esos valores
print("Personas: ")
for persona in personas:
    print("    " + str(persona))
# --- Read ---

#terminamos de medir el tiempo
fin = timeit.default_timer()
print('El tiempo de las operaciones fue de: ', fin - inicio)  

# eliminamos la BD para poder ejecutar sin problemas nuevamente el programa
cursor.execute(''' DROP TABLE IF EXISTS Persona ''')
conexion.commit()