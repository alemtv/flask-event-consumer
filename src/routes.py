from flask import request
from flask_restx import Resource
import json
from config import PAYLOADS_FILE
from src import api, events_name_space
from src.models import event_model


@events_name_space.route("/")
class EventsMainClass(Resource):
    @api.doc(responses={200: 'OK',
                        201: 'Created',
                        400: 'Bad Request',
                        500: 'Internal Server Error'})
    @api.expect(event_model, validate=True)
    def post(self):
        if request.is_json:
            try:
                # save incoming payloads to a file
                with open(PAYLOADS_FILE, 'a') as file:
                    json.dump(request.json, file)
                    file.write('\n')
                    return {"message": "Event created successfully"}, 201
            except KeyError:
                events_name_space.abort(500,
                                        status="Could not save information",
                                        statusCode="500")
            except Exception:
                events_name_space.abort(400,
                                        status="Could not save information",
                                        statusCode="400")
        else:
            events_name_space.abort(400,
                                    status="Could not save information",
                                    statusCode="400")
