from flask import Blueprint, render_template, request
from identificador_animales import identificar_animal

main_controller = Blueprint('main', __name__)

@main_controller.route('/')
def home():
    return render_template('index.html')
    

@main_controller.route('/identificar', methods=['POST'])
def identificar():
    foto = request.files.get('foto')
    info_animales = {
        'Perro': {
            'nombre': 'Perro',
            'descripcion': 'El perro es un mamífero doméstico, conocido por su lealtad y compañía.',
            'cientifico': 'Canis lupus familiaris',
            'habitat': 'Doméstico, urbano y rural',
            'alimentacion': 'Omnívoro',
            'icono': '🐶'
        },
        'Gato': {
            'nombre': 'Gato',
            'descripcion': 'El gato es un felino doméstico, ágil y curioso, popular como mascota.',
            'cientifico': 'Felis catus',
            'habitat': 'Doméstico, urbano y rural',
            'alimentacion': 'Carnívoro',
            'icono': '🐱'
        },
        'Ave': {
            'nombre': 'Ave',
            'descripcion': 'Las aves son animales vertebrados de sangre caliente, con plumas y alas.',
            'cientifico': 'Aves (clase)',
            'habitat': 'Diversos: bosques, selvas, ciudades',
            'alimentacion': 'Omnívoro, granívoro, insectívoro, etc.',
            'icono': '🐦'
        },
        'Serpiente': {
            'nombre': 'Serpiente',
            'descripcion': 'Las serpientes son reptiles sin extremidades, muchas de ellas venenosas.',
            'cientifico': 'Serpentes (suborden)',
            'habitat': 'Selvas, desiertos, bosques, zonas urbanas',
            'alimentacion': 'Carnívoro',
            'icono': '🐍'
        },
        'Zorrillo': {
            'nombre': 'Zorrillo',
            'descripcion': 'El zorrillo es conocido por su capacidad de liberar un olor fuerte como defensa.',
            'cientifico': 'Mephitidae (familia)',
            'habitat': 'Bosques, campos, zonas urbanas',
            'alimentacion': 'Omnívoro',
            'icono': '🦨'
        },
        'Iguana': {
            'nombre': 'Iguana',
            'descripcion': 'La iguana es un reptil herbívoro, común en zonas tropicales.',
            'cientifico': 'Iguana iguana',
            'habitat': 'Selvas, zonas tropicales',
            'alimentacion': 'Herbívoro',
            'icono': '🦎'
        },
        'Vaca': {
            'nombre': 'Vaca',
            'descripcion': 'La vaca es un mamífero rumiante doméstico, criado principalmente para la producción de leche y carne.',
            'cientifico': 'Bos taurus',
            'habitat': 'Pastizales, granjas, zonas rurales',
            'alimentacion': 'Herbívoro',
            'icono': '🐄'
        },
        'Oveja': {
            'nombre': 'Oveja',
            'descripcion': 'La oveja es un mamífero doméstico criado principalmente por su lana, carne y leche.',
            'cientifico': 'Ovis aries',
            'habitat': 'Pastizales, montañas, granjas',
            'alimentacion': 'Herbívoro',
            'icono': '🐑'
        },
        'Chivo': {
            'nombre': 'Cabra',
            'descripcion': 'La cabra es un mamífero doméstico ágil y resistente, criado por su leche, carne y fibra.',
            'cientifico': 'Capra hircus',
            'habitat': 'Montañas, zonas áridas, granjas',
            'alimentacion': 'Herbívoro',
            'icono': '🐐'
        },
        'Cerdo': {
            'nombre': 'Cerdo',
            'descripcion': 'El cerdo es un mamífero doméstico inteligente, criado principalmente para la producción de carne.',
            'cientifico': 'Sus scrofa domesticus',
            'habitat': 'Granjas, corrales, zonas rurales',
            'alimentacion': 'Omnívoro',
            'icono': '🐖'
        }
    }
    if foto:
        resultados = identificar_animal(foto)
        # Solo mostrar el animal con mayor probabilidad
        animal, prob = max(resultados, key=lambda x: x[1])
        info = info_animales.get(animal, None)
        if info:
            resultado = (
                f"{info['icono']} {info['nombre']}<br>"
                f"Nombre científico: {info['cientifico']}<br>"
                f"Hábitat: {info['habitat']}<br>"
                f"Alimentación: {info['alimentacion']}<br>"
                f"Descripción: {info['descripcion']}"
            )
        else:
            resultado = f"{animal} ({prob:.2f}%)"
    else:
        resultado = "No se recibió imagen"
    return render_template('index.html', resultado=resultado)

@main_controller.route('/realidad-aumentada/<animal>', methods=['GET'])
def realidad_aumentada(animal):
    ar_models = {
        'Perro': {
            'src': 'https://cdn.jsdelivr.net/gh/aframe-models/animal-dog/scene.gltf',
            'scale': '1 1 1',
            'rotation': '0 180 0'
        },
        'Gato': {
            'src': 'https://cdn.jsdelivr.net/gh/aframe-models/animal-cat/scene.gltf',
            'scale': '1 1 1',
            'rotation': '0 180 0'
        },
        'Ave': {
            'src': 'https://cdn.jsdelivr.net/gh/aframe-models/animal-bird/scene.gltf',
            'scale': '1 1 1',
            'rotation': '0 180 0'
        },
        'Serpiente': {
            'src': 'https://cdn.jsdelivr.net/gh/aframe-models/animal-snake/scene.gltf',
            'scale': '1 1 1',
            'rotation': '0 180 0'
        },
        'Zorrillo': {
            'src': 'https://cdn.jsdelivr.net/gh/aframe-models/animal-skunk/scene.gltf',
            'scale': '1 1 1',
            'rotation': '0 180 0'
        },
        'Iguana': {
            'src': 'https://cdn.jsdelivr.net/gh/aframe-models/animal-iguana/scene.gltf',
            'scale': '1 1 1',
            'rotation': '0 180 0'
        }
    }
    ar_model = ar_models.get(animal.capitalize(), None)
    if not ar_model:
        return "Modelo AR no encontrado", 404
    return render_template('realidad_aumentada.html', ar_model=ar_model)
