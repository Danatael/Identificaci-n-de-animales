import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import tempfile
import os

# Cargar el modelo solo una vez
model = MobileNetV2(weights='imagenet')

def identificar_animal(imagen_file):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    try:
        imagen_file.save(tmp.name)
        img = image.load_img(tmp.name, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = model.predict(x)
        resultados = decode_predictions(preds, top=5)[0]

        # Definir palabras clave para cada animal
        animales = {
            'perro': ['dog'],
            'gato': ['cat'],
            'ave': ['bird', 'parrot', 'finch', 'cockatoo', 'macaw', 'jay', 'magpie', 'chickadee', 'bulbul', 'warbler', 'sparrow', 'robin', 'oriole', 'canary', 'goldfinch', 'cardinal', 'bunting', 'nuthatch', 'woodpecker', 'kingfisher', 'hummingbird', 'ostrich', 'penguin', 'goose', 'duck', 'swan', 'crane', 'stork', 'heron', 'flamingo', 'cock', 'hen', 'chicken', 'turkey', 'peacock', 'quail', 'ptarmigan', 'grouse', 'partridge', 'pigeon', 'dove', 'cuckoo', 'owl', 'hawk', 'eagle', 'vulture', 'falcon'],
            'serpiente': ['snake', 'python', 'boa', 'viper', 'cobra', 'mamba', 'rattlesnake', 'asp'],
            'zorrillo': ['skunk'],
            'iguana': ['iguana'],
            'vaca': ['cow', 'ox', 'bull', 'calf', 'cattle', 'steer', 'heifer'],
            'oveja': ['sheep', 'lamb', 'ram'],
            'chivo': ['goat', 'kid', 'billy'],
            'cerdo': ['pig', 'swine', 'hog', 'boar'],
            
        }

        filtrados = []
        for (_, nombre, prob) in resultados:
            nombre_lower = nombre.lower()
            for animal, keywords in animales.items():
                for k in keywords:
                    if k.lower() in nombre_lower:
                        filtrados.append((animal.capitalize(), prob*100))
                        break
        if not filtrados:
            return [('No se detectó ningún animal conocido', 0)]
        return filtrados
    except Exception as e:
        return [("Error al procesar la imagen", 0)]
    finally:
        tmp.close()
        if os.path.exists(tmp.name):
            os.remove(tmp.name)