from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship
from enums.livros import Genero
from typing import Union
from  model import Base

class Livro(Base):
    __tablename__ = 'livro'

    id = Column('pk_livro', Integer, primary_key=True)
    titulo = Column(String(140), nullable=False)
    autor = Column(String(140), nullable=True)
    lancamento = Column(DateTime, nullable=False)
    genero = Column(Enum(Genero), nullable=False)
    disponivel = Column(Boolean, nullable=False)

    emprestimos = relationship("Emprestimo", back_populates="livro")

    def __init__(self, titulo:str, autor:Union[str, None], lancamento:DateTime, genero:Genero):
        """
        Cria um Livro

        Arguments:
            titulo: nome do livro.
            autor: autor do livro.
            lancamento: data em que o livro foi lançado.
            genero: genero do livro.
            disponivel: se o livro está disponivel para emprestimo.
        """
        self.titulo = titulo
        self.lancamento = lancamento
        self.genero = genero
        self.disponivel = True

        if autor:
            self.autor = autor

    def disponivel_status(self, status:bool):
        self.disponivel = status
