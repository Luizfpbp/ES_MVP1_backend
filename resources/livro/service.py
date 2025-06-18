from resources.livro.dto import LivroDTO
from model import Session, Livro
from .schema import LivroSchema
from datetime import datetime
from logger import logger
from typing import List


class LivroService():
    livroSession = Session()

    def get_livros(self):
        logger.debug("Coletando livros...")

        livros: List[Livro] = self.livroSession.query(Livro).all()
        if not livros:
            logger.debug("Nenhum livro encontrado")
            return {"values": []}, 200
        else:
            logger.debug(f"%d livros encontrados" % len(livros))
            return {"values": 
                    [LivroDTO.from_orm(item).dict() for item in livros]}, 200
        
    def add_livro(self, form: LivroSchema):
        try:
            logger.debug(f"Criando livro com os dados {form}")

            lancamento = datetime.strptime(form.lancamento, "%d/%m/%Y")
            livro: Livro = Livro(form.titulo, form.autor, lancamento, form.genero)
            self.livroSession.add(livro)
            self.livroSession.commit()

            logger.debug("Livro criado")

            return LivroDTO.from_orm(livro).dict(), 200
        
        except Exception as error:
            error_msg = "Não foi possível salvar o Livro"
            logger.warning(f"Erro ao criar o livro, {error}")
            return {"mesage": error_msg}, 400