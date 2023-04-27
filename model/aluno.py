from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from typing import Union

from model import Base


class Aluno(Base):
    __tablename__ = 'aluno'

    id = Column("pk_aluno", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    idade = Column(Integer)
    matricula = Column(Integer, unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, idade:int, matricula:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um(a) Aluno(a)

        Arguments:
            nome: nome do aluno.
            idade: idade do aluno.
            matricula: matricula do aluno.
            data_insercao: data de quando o aluno(a) foi inserido à turma
        """
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

