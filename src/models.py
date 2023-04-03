from flask_restx import fields
from src import api

event_model = api.model('Event Model', {
            'event_type': fields.String(required=True,
                                        description="Event type",
                                        help="Cannot be blank."),
            'event_payload': fields.String(required=True,
                                           description="Event payload",
                                           help="Cannot be blank.")
            })
