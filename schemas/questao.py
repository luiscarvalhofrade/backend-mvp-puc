from pydantic import BaseModel


class QuestaoSchema(BaseModel):
    """ Define como uma nova questao a ser inserida deve ser representada
    """
    materia_id: int = 1
    professor_id: int = 7
    lista_id: int = 5
    descricao: str = "Encontre o valor de X"