import os
import unittest

from app.models.eventos import Base, MySession
from app.models.eventos import Evento

class TestModel(unittest.TestCase):
    def setUp(self):
        mysession = MySession(Base, test=True)
        self.session = mysession.session
        self.engine = mysession.engine
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_evento(self):
        evento = Evento()
        evento.codigorecinto = '0001'
        self.session.add(evento)
        self.session.commit()
        oid = evento.id
        evento_copia = self.session.query(Evento).filter_by(id=oid).first()
        assert evento is evento_copia
