# Aquí irán los modelos para identificar animales
# Por ejemplo, clases o funciones para cargar modelos de IA
from flask import Blueprint, render_template, request
from identificador_animales import identificar_animal

main_controller = Blueprint('main', __name__)

@main_controller.route('/')
def home():
    return render_template('index.html')
    
@main_controller.route('/identificar', methods=['POST'])
def identificar():
    foto = request.files.get('foto')
    if foto:
        resultados = identificar_animal(foto)
        resultado = "Resultados:<br>" + "<br>".join([f"{nombre}: {prob:.2f}%" for nombre, prob in resultados])
    else:
        resultado = "No se recibió imagen"
    return render_template('index.html', resultado=resultado)