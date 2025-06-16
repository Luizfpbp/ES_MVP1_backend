from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from model import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column("pk_usuario", Integer, primary_key=True)
    nome = Column(String(140))
    email = Column(String(140), unique=True)
    data_nascimento = Column(DateTime)

    emprestimos = relationship("Emprestimo", back_populates="usuario")

    def __init__(self, nome:str, email:int, data_nascimento:DateTime):
        """
        Cria um Usuário

        Arguments:
            nome: nome do usuário.
            email: email do usuário.
            data_nascimento: data de nascimento do usuário.
        """
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento