from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model import Base


class Questao(Base):
    __tablename__ = 'questao'

    id = Column("pk_questao", Integer, primary_key=True)
    descricao = Column(String(3000), unique=True, nullable=False)
    materia = Column(Integer, ForeignKey("materia.pk_materia"), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())
    lista = Column(Integer, ForeignKey("lista.pk_lista"))
    professor = Column(Integer, ForeignKey("professor.pk_professor"), nullable=False)

    def __init__(self, descricao:str, materia:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma questao

        Arguments:
            descricao: texto da questao.
            materia: materia(s) atrelada(s) a questao.
            data_insercao: data de quando a questao foi inserida
        """
        self.descricao = descricao
        self.materia = materia

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao