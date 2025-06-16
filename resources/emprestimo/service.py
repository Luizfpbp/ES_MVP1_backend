from .schema import EmprestimoSchema, EndEmprestimoSchema
from model import Session, Emprestimo, Usuario, Livro
from resources.emprestimo.dto import EmprestimoDTO
from typing import List


class EmprestimoService():
    emprestimoSession = Session()
    
    def get_emprestimos(self):
        emprestimos: List[Emprestimo] = self.emprestimoSession.query(Emprestimo).all()
        if not emprestimos:
            return {"values": []}, 200
        else:
            return {"values": 
                    [EmprestimoDTO.from_orm(item).dict() for item in emprestimos]}, 200
        
    def add_emprestimo(self, form:EmprestimoSchema):
        try:
            
            usuario: Usuario = self.emprestimoSession.query(Usuario).filter(Usuario.id == form.usuario_id).first()
            livro: Livro = self.emprestimoSession.query(Livro).filter(Livro.id == form.livro_id).first()

            if not usuario:
                error_msg = "Usuário não encontrado"
                return {"message": error_msg}, 404
            
            if not livro:
                error_msg = "Livro não encontrado"
                return {"message": error_msg}, 404

            emprestimo: Emprestimo = Emprestimo(usuario, livro)

            self.emprestimoSession.add(emprestimo)
            livro.disponivel_status(False)
            self.emprestimoSession.commit()
            return EmprestimoDTO.from_orm(emprestimo).dict(), 200
        
        except Exception as e:
            error_msg = "Não foi possível criar o emprestimo"
            return {"mesage": error_msg}, 400
    
    def end_emprestimo(self, form:EndEmprestimoSchema):
        try:
            emprestimo: Emprestimo = self.emprestimoSession.query(Emprestimo).filter(Emprestimo.id == form.emprestimo_id).first()
            if not emprestimo:
                error_msg = "Empréstimo não encontrado"
                return {"message": error_msg}, 404
            
            if emprestimo.devolvido:
                error_msg = "Empréstimo já foi finalizado"
                return {"message": error_msg}, 400
            
            emprestimo.retornar_livro()
            emprestimo.livro.disponivel_status(True)
            self.emprestimoSession.commit()
            return EmprestimoDTO.from_orm(emprestimo).dict(), 200
        
        except Exception as e:
            print(e)
            error_msg = "Não foi possível finalizar o empréstimo"
            return {"mesage": error_msg}, 400