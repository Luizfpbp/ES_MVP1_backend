from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from enums.livros import Genero

class LivroDTO(BaseModel):
    id: int
    titulo: str
    autor: Optional[str]
    lancamento: datetime
    genero:Genero
    disponivel:bool

    class Config:
        orm_mode = True
        use_enum_values = True