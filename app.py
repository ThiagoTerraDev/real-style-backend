from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Produto 
from logger import logger
from schemas import *
from flask_cors import CORS


info = Info(title="Real Style Backend", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, ReDoc ou RapiDoc.")
produto_tag = Tag(name="Produto", description="Consulta, adição, remoção ou edição de produtos cadastrados na base.")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def adiciona_produto(form: ProdutoSchema):
    """Adiciona um novo produto à base de dados.

    Retorna uma representação do produto.
    """
    produto = Produto(
        nome=form.nome,
        quantidade=form.quantidade,
        valor_unitario=form.valor_unitario)
    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200
    
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já cadastrado na base."
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 409
    
    except Exception as e:
        # caso ocorra um erro fora do previsto
        error_msg = "Não foi possível cadastrar novo item."
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """ Faz a busca por todos os produtos cadastrados.

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produtos = session.query(Produto).all()

    if not produtos:
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d produtos encontrados" % len(produtos))
        # retorna a representação de produto
        print(produtos)
        return apresenta_produtos(produtos), 200


@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """ Faz a busca por um produto a partir do nome do produto.

    Retorna uma representação do produto.
    """
    produto_nome = query.nome
    logger.debug(f"Coletando dados sobre o produto #{produto_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produto = session.query(Produto).filter(Produto.nome == produto_nome).first()

    if not produto:
        error_msg = "Produto não encontrado na base."
        logger.warning(f"Erro ao buscar produto '{produto_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Produto encontrado: '{produto_nome}'")
        # retorna a representação do produto
        return apresenta_produto(produto), 200


@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def deleta_produto(query: ProdutoBuscaSchema):
    """ Deleta um produto a partir do nome do produto informado.

    Retorna uma mensagem de confirmação de remoção.
    """
    produto_nome = unquote(unquote(query.nome))
    print(produto_nome)
    logger.debug(f"Deletando dados sobre o produto #{produto_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Produto).filter(Produto.nome == produto_nome).delete()
    session.commit()

    if count:
        logger.debug(f"Deletando produto #{produto_nome}")
        return {"message": "Produto removido", "nome": produto_nome}, 200
    else:
        error_msg = "Produto não encontrado na base."
        logger.warning(f"Erro ao deletar produto #'{produto_nome}', {error_msg}")
        return {"message": error_msg}, 404
