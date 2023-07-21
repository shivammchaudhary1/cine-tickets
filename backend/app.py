from flask import Flask
from config import SECRET_KEY, DEBUG
from routes.user_routes import user_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DEBUG'] = DEBUG

# Register the user blueprint
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()
