from pydantic import BaseModel


class ListaSchema(BaseModel):
    """ Define como uma nova lista a ser inserida deve ser representada
    """
    materia_id: int = 1
    nome: str = "Lista 1 - Matemarica"