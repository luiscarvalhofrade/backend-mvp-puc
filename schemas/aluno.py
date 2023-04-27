from pydantic import BaseModel
from typing import Optional, List
from model.aluno import Aluno


class AlunoSchema(BaseModel):
    """ Define como um novo aluno(a) a ser inserido deve ser representado
    """
    nome: str = "Foo Bar"
    idade: int = 12
    matricula: int = 12345


class AlunoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do aluno(a).
    """
    nome: str = "Teste"


class ListagemAlunosSchema(BaseModel):
    """ Define como uma listagem de alunos será retornada.
    """
    alunos:List[AlunoSchema]


def apresenta_alunos(alunos: List[Aluno]):
    """ Retorna uma representação do aluno(a) seguindo o schema definido em
        AlunoViewSchema.
    """
    result = []
    for aluno in alunos:
        result.append({
            "nome": aluno.nome,
            "idade": aluno.idade,
            "matricula": aluno.matricula,
        })

    return {"alunos": result}


class AlunoViewSchema(BaseModel):
    """ Define como um aluno(a) será retornado: aluno.
    """
    id: int = 1
    nome: str = "Foo Bar"
    idade: int = 12
    matricula: int = 12345

class AlunoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_aluno(aluno: Aluno):
    """ Retorna uma representação do aluno(a) seguindo o schema definido em
        AlunoViewSchema.
    """
    return {
        "id": aluno.id,
        "nome": aluno.nome,
        "idade": aluno.idade,
        "matricula": aluno.matricula,
    }
