from flask import Blueprint, render_template, request
from Models.index import identificar_animal

main_controller = Blueprint('main', __name__)

@main_controller.route('/')
def home():
    return render_template('index.html')
    

@main_controller.route('/identificar', methods=['POST'])
def identificar():
    foto = request.files.get('foto')
    if foto:
        try:
            resultado = identificar_animal(foto)
        except Exception as e:
            resultado = f"Error al procesar la imagen: {str(e)}"
    else:
        resultado = "No se recibió imagen"
    return render_template('index.html', resultado=resultado)
