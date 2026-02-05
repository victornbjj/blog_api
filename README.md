# blog_api

REST API completa para um blog fantasia usando Flask e SQLite.

## Requisitos
- Python 3.10+
- Flask

## Instalação
1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd blog_api
```
2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install flask
```

## Como executar
```bash
python app.py
```

A API ficará disponível em:
```bash
http://127.0.0.1:5000
```

## Endpoints

### Listar posts
- **GET** `/posts`

**Resposta (exemplo):**
```json
[
  {
    "id": 1,
    "titulo": "Meu post",
    "conteudo": "Conteúdo..."
  }
]
```

### Criar post
- **POST** `/posts`

**Body (JSON):**
```json
{
  "titulo": "Meu post",
  "conteudo": "Conteúdo..."
}
```

**Resposta (exemplo):**
```json
{
  "mensagem": "Post iniciado com sucesso!"
}
```

### Deletar post
- **DELETE** `/posts/<id>`

**Resposta (exemplo):**
```json
{
  "mensagem": "Post deletado com sucesso!"
}
```

## Testando com Postman
1. Inicie o servidor: `python app.py`
2. Crie uma requisição:
   - **POST** `http://127.0.0.1:5000/posts`
   - Header: `Content-Type: application/json`
   - Body:
```json
{
  "titulo": "Meu primeiro post",
  "conteudo": "Conteúdo do post"
}
```
3. Para listar:
   - **GET** `http://127.0.0.1:5000/posts`

## Estrutura do projeto
```
app.py
database.py
models.py
routes.py
```

## Licença
Este projeto está sob a licença MIT.
