# API: Criação de uma turma

Este pequeno projeto o backend da Disciplina **Desenvolvimento Full Stack Básico** desenvolvida por Luis Frade

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
(env)$ pip3 install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 9000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 9000 --reload
```

Abra o [http://localhost:9000/#/](http://localhost:9000/#/) no navegador para verificar o status da API em execução.
