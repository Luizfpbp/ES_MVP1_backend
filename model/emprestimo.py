from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from model import Base, Usuario, Livro

class Emprestimo(Base):
    __tablename__ = 'emprestimo'

    id = Column("pk_emprestimo", Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.pk_usuario"), nullable=False)
    livro_id = Column(Integer, ForeignKey("livro.pk_livro"), nullable=False)
    data_emprestimo = Column(DateTime, nullable=False)
    data_devolucao = Column(DateTime)
    devolvido = Column(Boolean, nullable=False)

    usuario = relationship("Usuario", back_populates="emprestimos")
    livro = relationship("Livro", back_populates="emprestimos")

    def __init__(self, usuario:Usuario, livro:Livro):
        """
        Cria uma relação de Emprestimo

        Arguments:
            usuario_id: usuário que está/esteve com o livro.
            livro_id: livro que foi emprestado
            data_emprestimo: data em que o livro foi emprestado
            data_devolução: data em que o livro foi entregue
        """
        self.data_emprestimo = datetime.now()
        self.usuario = usuario
        self.livro = livro
        self.devolvido = False

    def retornar_livro(self):
        self.data_devolucao = datetime.now()
        self.devolvido = True


