from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from enums.livros import Genero

class LivroSchema(BaseModel):
    """ 
    Define como um novo livro a ser inserido deve ser representado
    """
    titulo:str = "Titulo"
    autor:Optional[str] = "Jorge"
    lancamento:str = "10/06/2022"
    genero:Genero = Genero.COMEDIA

class LivroViewSchema(BaseModel):
    """ 
    Define como a visualização de um livro será retornada
    """
    id:int = 1
    titulo:str = "Titulo"
    autor:Optional[str] = "Jorge"
    lancamento:datetime = datetime.now()
    genero:Genero = Genero.COMEDIA
    disponivel:bool = True

class ListLivrosSchema(BaseModel):
    """ 
    Define como uma listagem de livros será retornada.
    """
    values:List[LivroViewSchema]