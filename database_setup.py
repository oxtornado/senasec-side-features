import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect("senasec.db")
cursor = conn.cursor()

# Crear tabla de usuarios autorizados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        face_id TEXT UNIQUE NOT NULL
    )
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Base de datos creada con éxito")
