from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model import Base


class professor(Base):
    __tablename__ = 'professor'

    id = Column("pk_professor", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    idade = Column(Integer)
    matricula = Column(Integer, unique=True)
    materia = Column(Integer, ForeignKey("materia.pk_materia"), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, idade:int, materia: int, matricula:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um(a) Professor(a)

        Arguments:
            nome: nome do(a) professor(a).
            idade: idade do(a) professor(a).
            matricula: matricula do(a) professor(a).
            materia: materia a qual o(a) professor(a) da aula.
            data_insercao: data de quando o(a) professor(a) foi inserido
        """
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.materia = materia

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

