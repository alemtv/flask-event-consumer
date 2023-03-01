from flask import Flask, request
from flask_restx import Api, Resource, fields
import json

flask_app = Flask(__name__)
api = Api(app = flask_app, 
          version = "1.0", 
          title = "Event consumer", 
          description = "The service should expose a HTTP API endpoint that accepts incoming JSON payloads and persists them to a file.")

name_space = api.namespace('events', description='Event consumer')

model = api.model('Event Model', {
            'event_type': fields.String(required = True,  description="Event type",  help="Cannot be blank."),
            'event_payload': fields.String(required = True, description="Event payload", help="Cannot be blank.")
            })

# get params from config file
with open('config.json','r') as config:
    params = json.load(config)
    print(f'Config params: {params}')

@name_space.route("/")
class MainClass(Resource):
    @api.doc(responses={ 200: 'OK', 201: 'Created', 400: 'Bad Request', 500: 'Internal Server Error'})   
    @api.expect(model, validate=True)    
    def post(self):
        if request.is_json:
            try:
                with open(params['payloads_file'], 'a') as file:
                    json.dump(request.json, file)
                    file.write('\n')
                    return {"message": "Event created successfully"}, 201
            except KeyError as e:
                name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
            except Exception as e:
                name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")
        else:
            name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")
    
if __name__ == '__main__':
    flask_app.run(host="127.0.0.1", port=8000, debug=True)