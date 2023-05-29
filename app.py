from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Aluno, Materia, Professor, Questoa, Lista
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="API Turma", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
aluno_tag = Tag(name="Aluno", description="Adição, visualização e remoção de alunos à turma")
materia_tag = Tag(name="Materia", description="Adição, visualização e remoção de mateira")
professor_tag = Tag(name="Professor", description="Adição, visualização e remoção de professor")
questao_tag = Tag(name="Questao", description="Adição, visualização e remoção de questao")
lista_tag = Tag(name="Lista", description="Adição, visualização e remoção de lista")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/aluno', tags=[aluno_tag],
          responses={"200": AlunoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_aluno(json: AlunoSchema):
    """Adiciona um novo Aluno à turma

    Retorna uma representação dos alunos.
    """
    aluno = Aluno(
        nome=json.nome,
        idade=json.idade,
        matricula=json.matricula)
    logger.debug(f"Adicionando aluno de nome: '{aluno.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando aluno(a)
        session.add(aluno)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado aluno(a): '{aluno.nome}'")
        return apresenta_aluno(aluno), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Aluno(a) de mesmo nome ou matricula já existe na turma"
        logger.warning(f"Erro ao adicionar aluno(a) '{aluno.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo(a) aluno(a) na turma"
        logger.warning(f"Erro ao adicionar aluno '{aluno.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/alunos', tags=[aluno_tag],
         responses={"200": ListagemAlunosSchema, "404": ErrorSchema})
def get_alunos():
    """Faz a busca por todos os Alunos(as) matriculados na turma

    Retorna uma representação da lista de alunos(as).
    """
    logger.debug(f"Coletando turma ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    alunos = session.query(Aluno).all()

    if not alunos:
        # se não há alunos cadastrados
        return {"alunos": []}, 200
    else:
        logger.debug(f"% de alunos encontrados" % len(alunos))
        # retorna a representação de alunos(as)
        print(alunos)
        return apresenta_alunos(alunos), 200

@app.delete('/aluno', tags=[aluno_tag],
            responses={"200": AlunoDelSchema, "404": ErrorSchema})
def del_aluno(query: AlunoBuscaSchema):
    """Deleta um(a) Aluno(a)

    Retorna uma mensagem de confirmação da remoção.
    """
    aluno_nome = unquote(unquote(query.nome))
    print(aluno_nome)
    logger.debug(f"Deletando dados sobre aluno #{aluno_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Aluno).filter(Aluno.nome == aluno_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado(a) aluno(a) #{aluno_nome}")
        return {"mesage": "Aluno(a) removido(a)", "id": aluno_nome}
    else:
        # se o aluno não foi encontrado
        error_msg = "Aluno(a) não encontrado(a) na turma"
        logger.warning(f"Erro ao deletar aluno(a) #'{aluno_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    
@app.post('/materia', tags=[materia_tag],
            responses={"200": MateriaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_materia(form: MateriaSchema):
    """Adiciona uma nova Materia

    Retorna uma representação das materias.
    """
    materia = Materia(
        nome=form.nome,
        idade=form.idade,
        matricula=form.matricula)
    logger.debug(f"Adicionando aluno de nome: '{aluno.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando aluno(a)
        session.add(aluno)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado aluno(a): '{aluno.nome}'")
        return apresenta_aluno(aluno), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Aluno(a) de mesmo nome ou matricula já existe na turma"
        logger.warning(f"Erro ao adicionar aluno(a) '{aluno.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo(a) aluno(a) na turma"
        logger.warning(f"Erro ao adicionar aluno '{aluno.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/alunos', tags=[aluno_tag],
         responses={"200": ListagemAlunosSchema, "404": ErrorSchema})
def get_alunos():
    """Faz a busca por todos os Alunos(as) matriculados na turma

    Retorna uma representação da lista de alunos(as).
    """
    logger.debug(f"Coletando turma ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    alunos = session.query(Aluno).all()

    if not alunos:
        # se não há alunos cadastrados
        return {"alunos": []}, 200
    else:
        logger.debug(f"% de alunos encontrados" % len(alunos))
        # retorna a representação de alunos(as)
        print(alunos)
        return apresenta_alunos(alunos), 200

@app.delete('/aluno', tags=[aluno_tag],
            responses={"200": AlunoDelSchema, "404": ErrorSchema})
def del_aluno(query: AlunoBuscaSchema):
    """Deleta um(a) Aluno(a)

    Retorna uma mensagem de confirmação da remoção.
    """
    aluno_nome = unquote(unquote(query.nome))
    print(aluno_nome)
    logger.debug(f"Deletando dados sobre aluno #{aluno_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Aluno).filter(Aluno.nome == aluno_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado(a) aluno(a) #{aluno_nome}")
        return {"mesage": "Aluno(a) removido(a)", "id": aluno_nome}
    else:
        # se o aluno não foi encontrado
        error_msg = "Aluno(a) não encontrado(a) na turma"
        logger.warning(f"Erro ao deletar aluno(a) #'{aluno_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
