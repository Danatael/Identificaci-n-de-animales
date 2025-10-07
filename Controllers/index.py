from flask import Blueprint, render_template, request

main_controller = Blueprint('main', __name__)

@main_controller.route('/')
def home():
    return render_template('index.html')
    
@main_controller.route('/identificar', methods=['POST'])
def identificar():
    foto = request.files.get('foto')
    if foto:
        # Aquí iría el procesamiento real de la imagen
        resultado = "Animal identificado: Ejemplo"
    else:
        resultado = "No se recibió imagen"
    return render_template('index.html', resultado=resultado)
