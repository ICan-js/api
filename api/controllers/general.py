from api import app

from flask import render_template


@app.route("/", methods=["GET"])
def home_route():
    """Handler da rota da página inicial da API
    :return:
    """

    return render_template("index.html")
