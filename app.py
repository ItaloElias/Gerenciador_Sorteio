from flask import Flask, render_template, request
from dicionario import rifa
import random

app = Flask(__name__)

# Dicionário de exemplo (resumido)
rifa = rifa

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        todos_numeros = [n for grupo in rifa for n in grupo]
        escolhido = random.choice(todos_numeros)
        nome = next(nome for grupo, nome in rifa.items() if escolhido in grupo)
        resultado = f"Número sorteado: {escolhido} - {nome}"
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
