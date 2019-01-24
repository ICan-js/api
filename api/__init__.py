from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

from api.controllers import general
