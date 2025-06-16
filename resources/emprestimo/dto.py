from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from resources.livro.dto import LivroDTO
from resources.usuario.dto import UsuarioDTO

class EmprestimoDTO(BaseModel):
    id: int
    data_emprestimo: datetime
    data_devolucao: Optional[datetime]
    devolvido: bool
    usuario: UsuarioDTO
    livro: LivroDTO

    class Config:
        orm_mode = True