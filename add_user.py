import sqlite3

def agregar_usuario(nombre, face_id):
    conn = sqlite3.connect("senasec.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO usuarios (nombre, face_id) VALUES (?, ?)", (nombre, face_id))
        conn.commit()
        print(f"✅ Usuario '{nombre}' agregado con éxito.")
    except sqlite3.IntegrityError:
        print(f"⚠️ El usuario '{nombre}' ya existe en la base de datos.")
    
    conn.close()

# Ejemplo de uso
agregar_usuario("Julian Camacho", "face_id_de_prueba")
