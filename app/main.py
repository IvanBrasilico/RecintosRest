from flask import Flask, jsonify
from models.eventos import Base, Evento, MySession
from views.api import register_api
from flasgger import Swagger




def configure_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    return app


mysession = MySession(Base, test=True)
session = mysession.session
engine = mysession.engine
Base.metadata.create_all(engine)
app = configure_app()


swagger = Swagger(app)
from flasgger import swag_from
@app.route('/evento/<id>/')
@swag_from('evento.yml')
def get_evento(id):
    evento = Evento.query.find_one(id==id)
    return jsonify(evento)

@app.route('/evento', methods=['POST'])
@swag_from('evento.yml')
def post_evento():
    evento = Evento.find_one(id==id)
    return jsonify(evento)


app.run(debug=True)



