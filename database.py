import sqlite3

data_base= 'blog.db'



def get_connection():
    return sqlite3.connect(data_base)




def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    





   