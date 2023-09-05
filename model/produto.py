from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from model import Base


class Produto(Base):
    __tablename__ = "produto"

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(250), unique=True)
    quantidade = Column(Integer)
    valor_unitario = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, quantidade:int, valor_unitario:float, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto.

        Arguments:
            nome: nome do produto.
            quantidade: quantidade que se espera comprar daquele produto.
            valor_unitario: valor esperado para a unidade do produto.
            data_insercao: data de quando o produto foi inserido à base.
        """
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

        # Se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
    