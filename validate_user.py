import sqlite3
import requests

# API de Imagga
API_KEY = "acc_d16ad7cfa498c09"
API_SECRET = "aa81b601db0eb05d7343c3bcfc8d7fe9"
IMAGGA_URL = "https://api.imagga.com/v2/faces/detections"

# Función para buscar usuario en la base de datos
def verificar_usuario(face_id):
    conn = sqlite3.connect("senasec.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nombre FROM usuarios WHERE face_id = ?", (face_id,))
    usuario = cursor.fetchone()
    
    conn.close()
    
    if usuario:
        return usuario[0]  # Retorna el nombre del usuario autorizado
    return None  # Si no está registrado

# Función para procesar la imagen y verificar si el usuario está permitido
def procesar_imagen(image_path):
    with open(image_path, "rb") as image_file:
        response = requests.post(
            IMAGGA_URL,
            auth=(API_KEY, API_SECRET),
            files={"image": image_file}
        )

    data = response.json()

    if "faces" in data.get("result", {}):
        for face in data["result"]["faces"]:
            face_id = str(face["coordinates"])  # Esto es temporal, ya que no tenemos Face ID único

            usuario = verificar_usuario(face_id)
            if usuario:
                print(f"✅ Acceso permitido para {usuario}")
                return True
            else:
                print("⛔ Acceso denegado")
                return False
    
    print("⚠️ No se detectó ningún rostro en la imagen")
    return False

# Ejemplo de uso
procesar_imagen("./images/julian-camacho.jpeg")
