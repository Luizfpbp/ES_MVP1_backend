from .schema import EmprestimoSchema, EndEmprestimoSchema
from model import Session, Emprestimo, Usuario, Livro
from resources.emprestimo.dto import EmprestimoDTO
from logger import logger
from typing import List


class EmprestimoService():
    emprestimoSession = Session()
    
    def get_emprestimos(self):
        logger.debug("Coletando emprestimos...")

        emprestimos: List[Emprestimo] = self.emprestimoSession.query(Emprestimo).order_by(Emprestimo.data_emprestimo.desc()).all()
        if not emprestimos:
            logger.debug("Nenhum emprestimo encontrado")
            return {"values": []}, 200
        else:
            logger.debug(f"%d emprestimos encontrados" % len(emprestimos))
            return {"values": 
                    [EmprestimoDTO.from_orm(item).dict() for item in emprestimos]}, 200
        
    def add_emprestimo(self, form:EmprestimoSchema):
        try:
            logger.debug(f"Criando emprestimo com os dados com os ids {form}")

            usuario: Usuario = self.emprestimoSession.query(Usuario).filter(Usuario.id == form.usuario_id).first()
            livro: Livro = self.emprestimoSession.query(Livro).filter(Livro.id == form.livro_id).first()

            if not usuario:
                error_msg = "Usuário não encontrado"
                logger.warning(f"Erro ao criar o emprestimo, {error_msg}")
                return {"message": error_msg}, 404
            
            if not livro:
                error_msg = "Livro não encontrado"
                logger.warning(f"Erro ao criar o emprestimo, {error_msg}")
                return {"message": error_msg}, 404

            emprestimo: Emprestimo = Emprestimo(usuario, livro)

            self.emprestimoSession.add(emprestimo)
            livro.disponivel_status(False)
            self.emprestimoSession.commit()

            logger.debug("Emprestimo criado")

            return EmprestimoDTO.from_orm(emprestimo).dict(), 200
        
        except Exception as error:
            error_msg = "Não foi possível criar o emprestimo"
            logger.warning(f"Erro ao criar o emprestimo, {error}")
            return {"mesage": error_msg}, 400
    
    def end_emprestimo(self, form:EndEmprestimoSchema):
        try:
            logger.debug(f"Finalizando o emprestimo de id {form}")

            emprestimo: Emprestimo = self.emprestimoSession.query(Emprestimo).filter(Emprestimo.id == form.emprestimo_id).first()
            if not emprestimo:
                error_msg = "Empréstimo não encontrado"
                logger.warning(f"Erro ao alterar o emprestimo, {error_msg}")
                return {"message": error_msg}, 404
            
            if emprestimo.devolvido:
                error_msg = "Empréstimo já foi finalizado"
                logger.debug(error_msg)
                return {"message": error_msg}, 400
            
            emprestimo.retornar_livro()
            emprestimo.livro.disponivel_status(True)
            self.emprestimoSession.commit()

            logger.debug("Emprestimo alterado com sucesso")

            return EmprestimoDTO.from_orm(emprestimo).dict(), 200
        
        except Exception as error:
            error_msg = "Não foi possível finalizar o empréstimo"
            logger.warning(f"Erro ao alterar o emprestimo, {error}")
            return {"mesage": error_msg}, 400