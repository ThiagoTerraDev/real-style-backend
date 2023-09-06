from pydantic import BaseModel
from typing import List
from model.produto import Produto


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Mens Casual Premium Slim Fit T-Shirts"
    quantidade: int = 3
    valor_unitario: float = 299.99


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado
    """
    id: int = 1
    nome: str = "Mens Casual Premium Slim Fit T-Shirts"
    quantidade: int = 3
    valor_unitario: float = 299.99


def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor_unitario": produto.valor_unitario
    }


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos: List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor_unitario": produto.valor_unitario,
            "id": produto.id,
        })
    
    return {"produtos": result}


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca.
        Que será feita apenas com base no nome do produto.
    """
    nome: str = "Mens Casual Premium Slim Fit T-Shirts"


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    message: str
    nome: str


class UpdateProdutoSchema(BaseModel):
    """ Define como um novo produto pode ser editado.
    """
    nome: str = "Mens Casual Premium Slim Fit T-Shirts"
    quantidade: int = 12
