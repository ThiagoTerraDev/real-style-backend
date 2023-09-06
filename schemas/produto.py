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
