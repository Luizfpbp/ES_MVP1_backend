from resources.livro.dto import LivroDTO
from .schema import LivroSchema
from model import Session, Livro
from datetime import datetime
from typing import List


class LivroService():
    livroSession = Session()

    def get_livros(self):
        livros: List[Livro] = self.livroSession.query(Livro).all()
        if not livros:
            return {"values": []}, 200
        else:
            return {"values": [LivroDTO.from_orm(item).dict() for item in livros]}, 200
        
    def add_livro(self, form: LivroSchema):

        try:
            lancamento = datetime.strptime(form.lancamento, "%d/%m/%Y")
            livro: Livro = Livro(form.titulo, form.autor, lancamento, form.genero)
            self.livroSession.add(livro)
            self.livroSession.commit()
            return LivroDTO.from_orm(livro).dict(), 200
        
        except Exception as e:
            print(e)
            error_msg = "Não foi possível salvar o Livro"
            return {"mesage": error_msg}, 400