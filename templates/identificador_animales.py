# identificador_animales.py
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import tempfile

# Cargar el modelo solo una vez
model = MobileNetV2(weights='imagenet')

def identificar_animal(imagen_file):
    # Guarda la imagen temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
        imagen_file.save(tmp.name)
        img = image.load_img(tmp.name, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = model.predict(x)
        resultados = decode_predictions(preds, top=3)[0]
        # Solo mostramos los nombres y probabilidades
        return [(nombre, prob*100) for (_, nombre, prob) in resultados]