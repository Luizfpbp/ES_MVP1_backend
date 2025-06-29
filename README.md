# Minha API - Backend do Sistema de Biblioteca

Este é o backend do projeto de biblioteca apresentado na disciplina **Desenvolvimento Full Stack Básico**.  
A API foi desenvolvida com Flask e fornece os serviços necessários para o funcionamento do sistema de front-end, como o cadastro de usuários, livros e controle de empréstimos.

---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

Ativar o ambiente virtual

```
$ python3 -m virtualenv venv
$ source venv/bin/activate
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

```
(env)$ pip install -r requirements.txt
```

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
