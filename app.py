from flask import Flask, jsonify
import os
from wikipediadata import getBirthdays, getData, getDeaths, getEventosHistoricos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/<dia>")
def hello(dia):
    return jsonify({"aniversarios": getBirthdays(dia), "mortes": getDeaths(dia), "eventos": getEventosHistoricos(dia)})


@app.route("/<dia>/resumo")
def resumo(dia):
    return jsonify({"aniversarios": getBirthdays(dia)[:5], "mortes": getDeaths(dia)[:5], "eventos": getEventosHistoricos(dia)[:5]})


@app.route("/<dia>/aniversarios")
def aniversariantes(dia):
    return jsonify(getBirthdays(dia))


@app.route("/<dia>/mortes")
def mortes(dia):
    return jsonify(getDeaths(dia))


@app.route("/<dia>/eventos")
def eventos(dia):
    return jsonify(getEventosHistoricos(dia))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
