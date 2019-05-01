import flask_restless
from models.eventos import Evento


def register_api(app, session):
    # Create the Flask-Restless API manager.
    manager = flask_restless.APIManager(app, session=session)

    # Create API endpoints, which will be available at /api/<tablename> by
    # default. Allowed HTTP methods can be specified as well.
    manager.create_api(Evento, methods=['GET', 'POST', 'DELETE'])

