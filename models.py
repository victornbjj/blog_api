class Post:
    def __init__(self, id, titulo, conteudo):
        self.id= id
        self.titulo= titulo
        self.conteudo = conteudo
        
        
        
    def to_dict(self):
        return{
            "id" : self.id,
            "titulo": self.titulo,
            "conteudo": self.conteudo
        }