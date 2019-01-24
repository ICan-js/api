import os
from api import app

from flask_cors import cross_origin

from flask import render_template, send_from_directory, jsonify


@app.route("/models/mobilenetv1", methods=["GET"])
def mobilenetv1():
    """Handler da página inicial do modelo de Mobilenet V1
    :return:
    """

    return render_template("mobilenetv1.html")


@app.route("/models/mobilenetv1/<file>", methods=["GET"])
@cross_origin()
def mobilenetv1_model(file):
    """Handler para a distribuição dos arquivos do modelo
    :param file:
    :return:
    """

    path = os.path.join(app.config["BASE_DIR"], "api/models/mobilenetv1")

    try:
        return send_from_directory(directory=path, filename=file)
    except:
        return jsonify({
            "error": True,
            "message": "Erro ao tentar recuperar os dados"
        })
