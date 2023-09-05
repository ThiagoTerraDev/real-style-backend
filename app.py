from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Produto 
from logger import logger
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
