from flask import Blueprint, request, jsonify
import sqlite3
from models import Post
from database import data_base





post_routes = Blueprint("post_routes", __name__)








def get_connection():
    return sqlite3.connect(data_base)





@post_routes.route("/posts", methods=["GET"])
def listar_posts():
    
    
    page = request.args.get('page',1, type= int)
    limit = request.args.get('limit', 10, type= int)
    
    
    
    offset = (page - 1) * limit        
    
    #contar o total 
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT (*) FROM posts")
    total = cursor.fetchone()[0]

  
    #buscar os posts com paginação
    cursor.execute("SELECT * FROM posts  ORDER BY id DESC LIMIT ? OFFSET  ?", (limit, offset))
    rows = cursor.fetchall()
    conn.close()

    posts = [
        Post(id=row[0], titulo=row[1], conteudo=row[2]).to_dict()
        for row in rows
    ]

    return jsonify({
        
        "posts": posts,
        "page": page,
        "limit" : limit,
        "total": total
    })






@post_routes.route("/posts", methods=["POST"])
def criar_post():
    data = request.get_json()

    if not data or "titulo" not in data or "conteudo" not in data:
        return jsonify({"mensagem": "Dados incompletos!"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO posts (titulo, conteudo) VALUES (?, ?)",
        (data["titulo"], data["conteudo"])
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Post criado com sucesso!"}), 201







@post_routes.route("/posts/<int:id>", methods=["PATCH"])
def atualizar_post(id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts WHERE id = ?", (id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({"mensagem": "Post não encontrado!"}), 404

    titulo_atual = data.get("titulo", row[1])
    conteudo_atual = data.get("conteudo", row[2])

    cursor.execute(
        "UPDATE posts SET titulo = ?, conteudo = ? WHERE id = ?",
        (titulo_atual, conteudo_atual, id)
    )

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Post atualizado com sucesso!"}), 200





@post_routes.route("/posts/<int:id>", methods=["DELETE"])
def deletar_post(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM posts WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Post deletado com sucesso!"}), 200
