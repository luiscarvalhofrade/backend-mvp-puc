from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model import Base

class Aluno(Base):
    __tablename__ = 'aluno'

    id = Column("pk_aluno", Integer, primary_key=True)
    pessoa = Column(Integer, ForeignKey("pessoa.pk_pessoa"), nullable=False)
    turma = Column(Integer, ForeignKey("turma.pk_turma"), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self,  pessoa:int, turma:int, 
                 data_insercao:Union[DateTime, None] = None,
                 ):
        """
        Cria um(a) Aluno(a)

        Arguments:
            pessoa: pessoa atrelada ao aluno
            turma: turmad do(a) aluno(a)
        """
        self.pessoa = pessoa
        self.turma = turma

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
                self.data_insercao = data_insercao