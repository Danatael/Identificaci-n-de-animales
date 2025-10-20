
## Web app para detectar animales

El comando flask run --cert=adhoc inicia Flask con HTTPS usando un certificado generado automáticamente (adhoc). 
Esto permite que navegadores móviles accedan a la cámara, ya que muchos requieren HTTPS.

Pasos para usarlo:

# En la terminal, navega a la carpeta de tu proyecto.
Ejecuta: 

$env:FLASK_APP="index.py"; flask run --cert=adhoc --host=0.0.0.0 --port=5000

Esto inicia el servidor Flask en HTTPS, accesible desde otros dispositivos en la red.

# Luego, accede desde tu celular a:

Ejemplo: https://192.168.137.62:5000

