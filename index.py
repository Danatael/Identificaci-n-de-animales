import os
from flask import Flask

app = Flask(__name__)


# Helper para leer booleans desde variables de entorno
def _get_config_bool(name, default=False):
    val = os.environ.get(name)
    if val is None:
        return default
    return val.lower() in ('1', 'true', 'yes', 'on')


# Importar controladores
from Controllers.index import main_controller
app.register_blueprint(main_controller)


if __name__ == "__main__":
    # Escuchar en 0.0.0.0 para ser accesible desde otros dispositivos en la red local
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    # Permitir activar/desactivar debug mediante variable DEBUG (o por FLASK_ENV)
    debug = _get_config_bool('DEBUG', True)
    # HTTPS support: you can enable HTTPS in three ways:
    # 1) Provide SSL_CERT_PATH and SSL_KEY_PATH environment variables that point to a PEM cert and key.
    # 2) Set USE_ADHOC_SSL=true to let Werkzeug create a temporary certificate (only for development and localhost).
    # 3) Leave disabled and use plain HTTP.

    use_https = _get_config_bool('USE_HTTPS', False)
    use_adhoc = _get_config_bool('USE_ADHOC_SSL', False)

    ssl_context = None
    if use_https:
        cert_path = os.environ.get('SSL_CERT_PATH')
        key_path = os.environ.get('SSL_KEY_PATH')
        if cert_path and key_path and os.path.exists(cert_path) and os.path.exists(key_path):
            ssl_context = (cert_path, key_path)
            print(f"Usando HTTPS con certificado: {cert_path} {key_path}")
        elif use_adhoc:
            # Werkzeug will generate an ad-hoc cert (only recommended for dev on localhost)
            ssl_context = 'adhoc'
            print("Usando HTTPS adhoc (certificado temporal generado por Werkzeug)")
        else:
            print("USE_HTTPS está activo, pero no se encontraron SSL_CERT_PATH/SSL_KEY_PATH. Usa USE_ADHOC_SSL=true para adhoc o proporciona rutas válidas.")

    # Ejecutar la app, opcionalmente con ssl_context
    if ssl_context:
        app.run(host=host, port=port, debug=debug, ssl_context=ssl_context)
    else:
        app.run(host=host, port=port, debug=debug)
