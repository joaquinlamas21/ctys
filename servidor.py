# servidor.py
# Servidor que conecta la página web con el asistente programado en Python.

from flask import Flask, request, jsonify, send_from_directory
from asistente import responder, estado_inicial

app = Flask(__name__, static_folder="web", static_url_path="")


@app.route("/")
def inicio():
    return send_from_directory("web", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    datos = request.get_json(silent=True) or {}
    mensaje = (datos.get("mensaje") or "").strip()
    estado = datos.get("estado") or estado_inicial()

    if not mensaje:
        return jsonify(error="mensaje vacio"), 400

    respuesta, estado = responder(mensaje, estado)
    return jsonify(respuesta=respuesta, estado=estado)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
