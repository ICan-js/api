import os
from api import app

from flask_cors import cross_origin

from flask import render_template, send_from_directory, jsonify


@app.route("/models/lecun98", methods=["GET"])
def lecun98():
    """Handler da página inicial do modelo de Lecun98
    """

    return render_template("lecun98.html")


@app.route("/models/lecun98/<file>")
@cross_origin()
def lecun98_model(file):
    """Endpoint para a recuperação dos arquivos do modelo LeNet-5
    ---
    parameters:
      - name: file
        in: path
        type: string
        enum: ['model.json', 'group1-shardXofN']
        required: true
        description: Os parâmetros podem variar desde o arquivo de especificação, até mesmo os arquivos contendo os pesos sinápticos do modelo. É recomendado que este seja consumido diretamente pelo Tensorflow.js.
    responses:
      200:
        description: Retorna o arquivo especificado na requisição
    deprecated: true
    """
    path = os.path.join(app.config["BASE_DIR"], "api/models/lecun98")

    try:
        return send_from_directory(directory=path, filename=file)
    except:
        return jsonify({
            "error": True,
            "message": "Erro ao tentar recuperar os dados"
        })
