from datetime import datetime
from pydantic import BaseModel

class UsuarioDTO(BaseModel):
    id: int
    nome: str
    email:str
    data_nascimento: datetime

    class Config:
        orm_mode = True