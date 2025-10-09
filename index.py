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
    app.run(host="0.0.0.0", port=5000, debug=True)

