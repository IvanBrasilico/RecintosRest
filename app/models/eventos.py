"""Modelo de dados necessário para Eventos."""
import os

from sqlalchemy import (Column, DateTime, Integer, String, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class MySession():
    """Sessão.

    Para definir a sessão com o BD na aplicação. Para os
    testes, passando o parâmetro test=True, um BD na memória
    """

    def __init__(self, base=Base, test=False, nomebase='eventos.db'):
        """Abre conexão."""
        if test:
            path = ':memory:'
        else:
            path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), nomebase)
            if os.name != 'nt':
                path = '/' + path
        self._engine = create_engine('sqlite:///' + path, convert_unicode=True)
        Session = sessionmaker(bind=self._engine)
        if test:
            self._session = Session()
        else:
            self._session = scoped_session(Session)
            base.metadata.bind = self._engine

    @property
    def session(self):
        """Sessão."""
        return self._session

    @property
    def engine(self):
        """Engine."""
        return self._engine


class Evento(Base):
    """Cópia dados sobre escala das extrações."""

    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True)
    CodigoRecinto = Column(String(11), unique=True)
    DataRecebimento = Column(DateTime())


if __name__ == '__main__':
    mysession = MySession(Base, test=False)
