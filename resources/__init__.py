# schema imports
from resources.emprestimo.schema import EmprestimoSchema, EndEmprestimoSchema, EmprestimoViewSchema, ListEmprestimoSchema
from resources.usuario.schema import UsuarioSchema, UsuarioViewSchema, ListUsuariosSchema
from resources.livro.schema import LivroSchema, LivroViewSchema, ListLivrosSchema

# service imports
from resources.emprestimo.service import EmprestimoService
from resources.usuario.service import UsuarioService
from resources.livro.service import LivroService

from resources.comentario import ComentarioSchema
from resources.produto import ProdutoSchema, ProdutoBuscaSchema, ProdutoViewSchema, \
                            ListagemProdutosSchema, ProdutoDelSchema, apresenta_produtos, \
                            apresenta_produto, apresenta_produtos
from resources.error import ErrorSchema
