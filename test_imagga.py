import requests

API_KEY = "acc_d16ad7cfa498c09"
API_SECRET = "aa81b601db0eb05d7343c3bcfc8d7fe9"

# Imagen a analizar (reemplázala con una tuya)
image_path = "./images/julian-camacho.jpeg"
# image_url = "https://tu-servidor.com/imagen_prueba.jpg"  # Alternativa con URL

# Endpoint de Imagga
url = "https://api.imagga.com/v2/faces/detections"

# Si usas una imagen local
with open(image_path, "rb") as image_file:
    response = requests.post(
        url,
        auth=(API_KEY, API_SECRET),
        files={"image": image_file}
    )

# Alternativa: Si usas una imagen en URL
# response = requests.get(url, auth=(API_KEY, API_SECRET), params={"image_url": image_url})

# Mostrar respuesta
print(response.json())
