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
        }
    }
    if foto:
        resultados = identificar_animal(foto)
        etiquetas = []
        for animal, prob in resultados:
            info = info_animales.get(animal, None)
            if info:
                etiquetas.append(
                    f"{info['icono']} {info['nombre']}<br>"
                    f"Nombre científico: {info['cientifico']}<br>"
                    f"Hábitat: {info['habitat']}<br>"
                    f"Alimentación: {info['alimentacion']}<br>"
                    f"Descripción: {info['descripcion']}"
                )
            else:
                etiquetas.append(f"{animal} ({prob:.2f}%)")
        resultado = '<br><br>'.join(etiquetas)
    else:
        resultado = "No se recibió imagen"
    return render_template('index.html', resultado=resultado)
