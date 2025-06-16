from datetime import datetime
from typing import List
from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    """ Define como um novo usuario a ser inserido deve ser representado
    """
    nome:str = "Usuário Teste"
    email:str = "usuario@email.com"
    data_nascimento:str = "10/06/2022"

class UsuarioViewSchema(BaseModel):
    """ Define como a visualização de um usuario será retornada
    """
    id:int = 1
    nome:str = "Usuário Teste"
    email:str = "usuario@email.com"
    data_nascimento:datetime = datetime.now()

class ListUsuariosSchema(BaseModel):
    """ Define como uma listagem de usuários será retornada.
    """
    values:List[UsuarioViewSchema]
