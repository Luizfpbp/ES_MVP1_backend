from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from enums.livros import Genero
from typing import Union
from  model import Base

class Livro(Base):
    __tablename__ = 'livro'

    id = Column('pk_livro', Integer, primary_key=True)
    titulo = Column(String(140), nullable=False)
    autor = Column(String(140), nullable=True)
    ano = Column(DateTime, nullable=False)
    genero = Column(Enum(Genero), nullable=False)
    disponivel = Column(Boolean, nullable=False)

    def __init__(self, titulo:str, autor:Union[str, None], ano:DateTime, genero:Genero):
        """
        Cria um Livro

        Arguments:
            titulo: nome do livro.
            autor: autor do livro.
            ano: ano em que o livro foi lançado.
            genero: genero do livro.
            disponivel: se o livro está disponivel para emprestimo.
        """
        self.titulo = titulo,
        self.ano = ano
        self.genero = genero
        self.disponivel = True

        if autor:
            self.autor = autor

    def novo_emprestimo(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True