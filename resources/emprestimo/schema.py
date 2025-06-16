
from datetime import datetime
from typing import List
from pydantic import BaseModel
from enums.livros import Genero
from model import Usuario, Livro
from resources.livro.dto import LivroDTO
from resources.usuario.dto import UsuarioDTO


class EmprestimoSchema(BaseModel):
    """ 
    Define como um novo emprestimo a ser inserido deve ser representado
    """
    usuario_id:str = "1"
    livro_id:str = "1" 

class EndEmprestimoSchema(BaseModel):
    """ 
    Define como um emprestimo a ser finalizado deve ser representado
    """
    emprestimo_id:str = "1"

class EmprestimoViewSchema(BaseModel):
    """ 
    Define como a visualização de um emprestimo será retornada
    """
    id:int = 1
    usuario_id:int = 1
    livro_id:int = 1
    data_emprestimo:datetime = datetime.now()
    data_devolucao:datetime = datetime.now()
    devolvido:bool = True

    usuario:UsuarioDTO 
    livro:LivroDTO 

class ListEmprestimoSchema(BaseModel):
    """ 
    Define como uma listagem de emprestimos será retornada.
    """
    values:List[EmprestimoViewSchema]