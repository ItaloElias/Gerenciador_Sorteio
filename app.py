from flask import Flask, render_template, request
from dicionario import participantes
import random

app = Flask(__name__)

# Dicionário de exemplo (resumido)
participantes = participantes

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        resultado = f"Número sorteado: {random.randint(1, 100)}"
    return render_template("index.html", resultado=resultado, participantes=participantes)

if __name__ == "__main__":
    app.run(debug=True)
