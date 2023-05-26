from pydantic import BaseModel
from typing import Optional, List
from model.professor import Professor


class ProfessorSchema(BaseModel):
    """ Define como um(a) novo(a) professor(a) a ser inserido deve ser representado
    """
    nome: str = "Foo Bar"
    idade: int = 12
    matricula: int = 12345
    materia: str = "Matematica"


class ProfessorBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do(a) professor(a).
    """
    nome: str = "Teste"


class ListagemProfessoresSchema(BaseModel):
    """ Define como uma listagem de professores será retornada.
    """
    professores:List[ProfessorSchema]


def apresenta_professores(professores: List[Professor]):
    """ Retorna uma representação do professor(a) seguindo o schema definido em
        ProfessorViewSchema.
    """
    result = []
    for professor in professores:
        result.append({
            "nome": professor.nome,
            "idade": professor.idade,
            "matricula": professor.matricula,
            "materia": professor.materia
        })

    return {"professores": result}


class ProfessorViewSchema(BaseModel):
    """ Define como um(a) professor(a) será retornado: professor.
    """
    id: int = 1
    nome: str = "Foo Bar"
    idade: int = 12
    matricula: int = 12345
    materia: str = "Matematica"

class ProfessorDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str
    matricula: int

def apresenta_professor(professor: Professor):
    """ Retorna uma representação do(a) professor(a) seguindo o schema definido em
        ProfessorViewSchema.
    """
    return {
        "id": professor.id,
        "nome": professor.nome,
        "idade": professor.idade,
        "matricula": professor.matricula,
        "materia": professor.materia
    }
