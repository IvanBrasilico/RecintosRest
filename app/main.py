from flask import Flask
from models.eventos import Base, MySession
from views.api import register_api


def configure_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    return app


mysession = MySession(Base, test=True)
session = mysession.session
engine = mysession.engine
Base.metadata.create_all(engine)
app = configure_app()
register_api(app, session)
app.run()

