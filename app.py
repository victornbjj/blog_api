from flask import Flask
from routes import post_routes
from database import init_db



app = Flask(__name__)


init_db()


app.register_blueprint(post_routes)


if __name__ == "__main__":
    app.run(debug=True)
    