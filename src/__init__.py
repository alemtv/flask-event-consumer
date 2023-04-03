from flask import Flask
from flask_restx import Api

flask_app = Flask(__name__)

api = Api(app=flask_app,
          version="1.0",
          title="Event consumer",
          description="The service should expose a HTTP API endpoint "
                      "that accepts incoming JSON payloads "
                      "and persists them to a file.")

events_name_space = api.namespace('events', description='Event consumer')

from src import routes
from src import models
