from flask import Flask

app = Flask(__name__)

# Importar controladores

from Controllers.index import main_controller
app.register_blueprint(main_controller)

if __name__ == "__main__":
    app.run(debug=True)
