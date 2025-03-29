import cv2

def capturar_imagen():
    cam = cv2.VideoCapture(0)  # Abre la cámara
    ret, frame = cam.read()  # Captura un solo frame

    if ret:
        cv2.imwrite("./images/captura.jpg", frame)  # Guarda la imagen
        print("✅ Imagen capturada con éxito")
    else:
        print("⚠️ Error al capturar la imagen")

    cam.release()  # Cierra la cámara

capturar_imagen()
