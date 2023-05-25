from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from model import Base


class Materia(Base):
    __tablename__ = 'materia'

    id = Column("pk_materia", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Materia

        Arguments:
            nome: nome da materia.
            data_insercao: data de quando a materia foi inserido
        """
        self.nome = nome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao