from sqlalchemy.exc import IntegrityError
from model import Session, Usuario
from resources.usuario.dto import UsuarioDTO
from .schema import UsuarioSchema
from datetime import datetime
from typing import List

class UsuarioService():
    usuarioSession = Session()
    
    def get_usuarios(self):
        usuarios: List[Usuario] = self.usuarioSession.query(Usuario).all()

        if not usuarios:
            return {"values": []}, 200
        else:
            return {"values": 
                    [UsuarioDTO.from_orm(item).dict() for item in usuarios]}, 200
        
    def add_usuario(self, form:UsuarioSchema):
        try:
            data_nascimento = datetime.strptime(form.data_nascimento, "%d/%m/%Y")
            usuario: Usuario = Usuario(nome=form.nome, email=form.email, data_nascimento=data_nascimento)
            self.usuarioSession.add(usuario)
            self.usuarioSession.commit()
            return UsuarioDTO.from_orm(usuario).dict(), 200
        
        except IntegrityError as error:
            error_msg = "Email já existente"
            return {"mesage": error_msg}, 409 
        
        except Exception as error:
            error_msg = "Não foi possível salvar o Usuário"
            print(error)
            return {"mesage": error_msg}, 400