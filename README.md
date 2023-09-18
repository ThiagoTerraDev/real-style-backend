# Real Style Backend

Este projeto faz parte do MVP da disciplina Sprint II: Desenvolvimento Back-end Avançado, pós-graduação PUC-Rio.

O objetivo desta aplicação é desempenhar o controle e a visualização das funcionalidades disponibilizadas pela loja fictícia 
chamada Real Style, a qual vende roupas e acessórios para os públicos masculino e feminino. É implementada uma API seguindo o padrão REST, 
sendo permitido ao usuário consultar, adicionar, deletar ou editar produtos cadastrados no banco de dados (aplicação do conceito CRUD).
Para a realização deste MVP, foi fixada, enquanto diretriz, a inclusão de um serviço consumido de uma API externa. Sendo assim, os dados 
referentes aos produtos de vestuário (como imagens, títulos e preços) foram consumidos diretamente da https://fakestoreapi.com/.

Principais tecnologias utilizadas:
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [OpenAPI3](https://swagger.io/specification/)
 - [SQLite](https://www.sqlite.org/index.html)

Diagrama da arquitetura da aplicação e estratégias de comunicação implementadas: https://1drv.ms/i/s!AvTc9X8DiWmVj_MvyWRtPXuzk9SUHA?e=R1WWPD



## Como executar


### Passo 1: Criando um ambiente virtual

Após clonar o repositório, abra um novo terminal e digite o seguinte comando:
```
python -m venv venv
```
> Este comando cria um novo ambiente virtual usando o módulo "venv" do Python.

Ative o ambiente virtual digitando o seguinte comando:
```
.\venv\Scripts\Activate.ps1   
```

---
### Passo 2: Executando a API

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório e ativar o ambiente virtual (veja o passo 1), é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.
```
(venv) pip install -r requirements.txt
```
> Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API, basta executar:
```
(venv) flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte. 
```
(venv) flask run --host 0.0.0.0 --port 5000 --reload
```

> Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t nome_da_sua_imagem .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, o seguinte comando:

```
$ docker run -p 5000:5000 nome_da_sua_imagem
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.
