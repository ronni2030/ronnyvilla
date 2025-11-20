import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Página principal HTML
@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Servicio en marcha</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #111;
                color: #0f0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                color: #0f0;
            }
            p {
                color: #0a0;
            }
            .card {
                padding: 20px;
                background: #222;
                border: 1px solid #0f0;
                border-radius: 10px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>✔ Servicio en marcha</h1>
            <p>Hola, ronny-villa! Tu servidor Flask está funcionando correctamente.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

# Función de ejemplo
def sumar(a, b):
    return a + b

@app.route("/sumar/<int:a>/<int:b>")
def suma_route(a, b):
    return jsonify({"result": sumar(a, b)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)