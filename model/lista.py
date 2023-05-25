from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, ARRAY
from datetime import datetime
from typing import Union

from model import Base


class Aluno(Base):
    __tablename__ = 'lista'

    id = Column("pk_lista", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    materia = Column(Integer, ForeignKey("materia.pk_materia"), nullable=False)
    questoes = Column(ARRAY(Integer, ForeignKey("questao.pk_questao")))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, materia:int, questoes:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma lista

        Arguments:
            nome: nome da lista.
            materia: materia atrelada a lista.
            questoes: array de questoes atreladas a lista.
            data_insercao: data de quando a lista foi inserida
        """
        self.nome = nome
        self.materia = materia
        self.questoes = questoes

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao