from flasgger import Swagger

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
swagger = Swagger(app)

app.config.from_object("config")

from api.controllers import general, mobilenetv1, lecun98
