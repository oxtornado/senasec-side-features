from deepface import DeepFace

def comparar_rostros():
    try:
        resultado = DeepFace.verify(
            "./images/captura.jpg", 
            "./images/daniel-duarte.jpeg",
            model_name="Facenet512",  # Mejor precisión
            enforce_detection=True  # Evita errores por imágenes sin rostro
        )
        
        if resultado["distance"] < 0.3:  # Más estricto
            print("✅ Acceso permitido")
        else:
            print("⛔ Acceso denegado")

    except Exception as e:
        print(f"⚠️ Error al comparar: {e}")

comparar_rostros()
