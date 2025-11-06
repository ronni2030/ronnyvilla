import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hola, ronny-villa! El servicio está en marcha."})

# función de ejemplo que ya tenías
def sumar(a, b):
    return a + b

@app.route("/sumar/<int:a>/<int:b>")
def suma_route(a, b):
    return jsonify({"result": sumar(a, b)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
