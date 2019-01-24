from api import app

from flask_cors import cross_origin

from flask import render_template, send_from_directory


@app.route("/models/lecun98", methods=["GET"])
def lecun98():
    """Handler da página inicial do modelo de Lecun98
    :return:
    """

    return render_template("lecun98.html")


@app.route("/models/lecun98/<file>")
@cross_origin()
def lecun98_model(file):
    """Handler para a distribuição dos arquivos do modelo
    :param file:
    :return:
    """

    return send_from_directory(directory="/models/lecun98", filename=file)
