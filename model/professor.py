from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base, Questao


class Professor(Base):
    __tablename__ = 'professor'

    id = Column("pk_professor", Integer, primary_key=True)
    pessoa = Column(Integer, ForeignKey("pessoa.pk_pessoa"), nullable=False)
    materia = Column(Integer, ForeignKey("materia.pk_materia"), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())
    questao = relationship("Questao")

    def __init__(self, pessoa:int, materia: int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um(a) Professor(a)

        Arguments:
            pessoa: pessoa atrelada ao professor
            materia: materia a qual o(a) professor(a) da aula
        """
        self.pessoa = pessoa
        self.materia = materia

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_questao(self, questao:Questao):
        """ Adiciona uma nova questao criada pelo(a) Professor(a)
        """
        self.questoes.append(questao)

