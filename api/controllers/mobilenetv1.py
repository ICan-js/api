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
    """Endpoint para a recuperação dos arquivos do modelo MobileNet V1
    ---
    parameters:
      - name: file
        in: path
        type: string
        enum: ['model.json', 'group1-shard1of6', 'group1-shard2of6', 'group1-shard3of6', 'group1-shard4of6', 'group1-shard5of6', 'group1-shard6of6']
        required: true
        description: Os parâmetros podem variar desde o arquivo de especificação, até mesmo os arquivos contendo os pesos sinápticos do modelo. É recomendado que este seja consumido diretamente pelo Tensorflow.js
    responses:
      200:
        description: Retorna o arquivo especificado na requisição
    """

    path = os.path.join(app.config["BASE_DIR"], "api/models/mobilenetv1")

    try:
        return send_from_directory(directory=path, filename=file)
    except:
        return jsonify({
            "error": True,
            "message": "Erro ao tentar recuperar os dados"
        })
