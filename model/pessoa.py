from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model import Base

class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column("pk_pessoa", Integer, primary_key=True)
    categoria = Column(Integer, ForeignKey("categoria.pk_categoria"), nullable=False)
    nome = Column(String(140), unique=True)
    matricula = Column(Integer, unique=True)
    data_de_nascimento = Column(DateTime)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, categoria:int, nome:str, matricula:int, 
                 data_de_nascimento:datetime, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Pessoa

        Arguments:
            categoria: professor | aluno | admin | coordenador
            nome: nome do pessoa
            matricula: matricula da pessoa
            data_de_nascimento: data de nascimento da pessoa
            data_insercao: data de quando pessoa foi inserido na base
        """

        
        self.categoria = categoria
        self.nome = nome
        self.matricula = matricula
        self.data_de_nascimento = data_de_nascimento

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
                self.data_insercao = data_insercao