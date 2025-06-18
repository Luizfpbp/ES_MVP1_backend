from resources.usuario.dto import UsuarioDTO
from sqlalchemy.exc import IntegrityError
from model import Session, Usuario
from .schema import UsuarioSchema
from datetime import datetime
from logger import logger
from typing import List

class UsuarioService():
    usuarioSession = Session()
    
    def get_usuarios(self):
        logger.debug("Coletando usuários...")

        usuarios: List[Usuario] = self.usuarioSession.query(Usuario).all()

        if not usuarios:
            logger.debug("Nenhum usuário encontrado")
            return {"values": []}, 200
        else:
            logger.debug(f"%d usuários encontrados" % len(usuarios))
            return {"values": 
                    [UsuarioDTO.from_orm(item).dict() for item in usuarios]}, 200
        
    def add_usuario(self, form:UsuarioSchema):
        try:
            logger.debug(f"Criando usuário com os dados {form}")

            data_nascimento = datetime.strptime(form.data_nascimento, "%d/%m/%Y")
            usuario: Usuario = Usuario(nome=form.nome, email=form.email, data_nascimento=data_nascimento)
            self.usuarioSession.add(usuario)
            self.usuarioSession.commit()

            logger.debug("Usuário criado")

            return UsuarioDTO.from_orm(usuario).dict(), 200
        
        except IntegrityError as error:
            error_msg = "Email já existente"
            logger.warning(f"Erro ao criar o emprestimo, {error_msg}")
            return {"mesage": error_msg}, 409 
        
        except Exception as error:
            error_msg = "Não foi possível salvar o Usuário"
            logger.warning(f"Erro ao criar o emprestimo, {error}")
            return {"mesage": error_msg}, 400