
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, decode_predictions, preprocess_input

# Cargar el modelo MobileNetV2 solo una vez
model = MobileNetV2(weights='imagenet')

def identificar_animal(imagen_bytes):
	"""
	Recibe imagen en bytes, regresa el nombre del animal identificado (gato, caballo, oveja, vaca, etc)
	"""
	img = Image.open(imagen_bytes).convert('RGB')
	img = img.resize((224, 224))
	arr = np.array(img)
	arr = np.expand_dims(arr, axis=0)
	arr = preprocess_input(arr)
	preds = model.predict(arr)
	decoded = decode_predictions(preds, top=3)[0]
	# Buscar si el resultado es uno de los animales de interés
	animales_interes = [
		'cat', 'tabby', 'tiger_cat', 'Persian_cat', 'Siamese_cat',
		'horse', 'Arabian_camel', 'ox', 'cow', 'bull', 'ram', 'sheep', 'goat', 'pig', 'hog', 'boar'
	]
	for _, nombre, prob in decoded:
		for animal in animales_interes:
			if animal in nombre:
				return f"{nombre.replace('_', ' ').capitalize()} ({round(prob*100, 1)}%)"
	# Si no es animal de interés, mostrar el top 1
	nombre, prob = decoded[0][1], decoded[0][2]
	return f"{nombre.replace('_', ' ').capitalize()} ({round(prob*100, 1)}%)"
