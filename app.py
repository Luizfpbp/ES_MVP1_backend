from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from resources import *

from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# services
borrowService = EmprestimoService()
userService = UsuarioService()
bookService = LivroService()

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
usuario_tag = Tag(name="Usuario", description="Adição e visualização de usuários à base")
livro_tag = Tag(name="Livro", description="Adição e visualização de um livro cadastrado na base")
emprestimo_tag = Tag(name="Emprestimo", description="Adição e visualização de emprestimos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/usuario', tags=[usuario_tag], 
          responses={"200": UsuarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_usuario(form: UsuarioSchema):
    """
    Adiciona um novo Usuário à base de dados
    Retorna uma representação do usuário.
    """
    return userService.add_usuario(form)

@app.get('/usuarios', tags=[usuario_tag],
         responses={"200": ListUsuariosSchema, "404": ErrorSchema})
def get_usuarios():
    """
    Faz a busca por todos os Usuários cadastrados
    Retorna uma representação da listagem de usuários.
    """
    return userService.get_usuarios()

@app.post('/livro', tags=[livro_tag], 
          responses={"200": LivroViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_livro(form: LivroSchema):
    """
    Adiciona um novo Livro à base de dados
    Retorna uma representação do livro.
    """
    return bookService.add_livro(form)

@app.get('/livros', tags=[livro_tag],
         responses={"200": ListLivrosSchema, "404": ErrorSchema})
def get_livros(query: GetLivrosSchema):
    """
    Faz a busca por todos os Livros cadastrados
    Retorna uma representação da listagem de livros.
    """
    return bookService.get_livros(query)

@app.post('/emprestimo', tags=[emprestimo_tag],
          responses={"200": EmprestimoViewSchema, "404": ErrorSchema})
def add_emprestimo(form: EmprestimoSchema):
    """
    Adiciona um novo Emprestimo à base de dados
    Retorna uma representação do emprestimo.
    """
    return borrowService.add_emprestimo(form)

@app.put('/emprestimo/devolver', tags=[emprestimo_tag],
          responses={"200": EmprestimoViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def end_emprestimo(form: EndEmprestimoSchema):
    """
    Finaliza um Emprestimo a partir do id do emprestimo informado
    Retorna uma representação do emprestimo finalizado.
    """
    return borrowService.end_emprestimo(form)

@app.get('/emprestimos', tags=[emprestimo_tag],
         responses={"200": ListEmprestimoSchema, "404": ErrorSchema})
def get_emprestimos():
    """
    Faz a busca por todos os Emprestimos cadastrados
    Retorna uma representação da listagem de emprestimos.
    """
    return borrowService.get_emprestimos()