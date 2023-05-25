from pydantic import BaseModel
from typing import Optional, List
from model.materia import Materia


class MateriaSchema(BaseModel):
    """ Define como uma nova materia a ser inserido deve ser representado
    """
    nome: str = "Matematica"


class MateriaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da materia.
    """
    nome: str = "Matematica"


class ListagemMateriaSchema(BaseModel):
    """ Define como uma listagem de matérias será retornada.
    """
    materias:List[MateriaSchema]


def apresenta_materias(materias: List[Materia]):
    """ Retorna uma representação da materia seguindo o schema definido em
        MateriaViewSchema.
    """
    result = []
    for materia in materias:
        result.append({
            "nome": materia.nome
        })

    return {"materias": result}


class MateriaViewSchema(BaseModel):
    """ Define como materia será retornado: materia.
    """
    id: int = 1
    nome: str = "Portugues"

class MateriaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_materia(materia: Materia):
    """ Retorna uma representação da materia seguindo o schema definido em
        MateriaViewSchema.
    """
    return {
        "id": materia.id,
        "nome": materia.nome
    }