from flask import Flask
from config import config
from routes.movie_routes import movie_bp
from routes.event_routes import event_bp
from routes.user_routes import user_bp
from routes.theater_routes import theater_bp
from routes.booking_routes import booking_bp

app = Flask(__name__)
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['DEBUG'] = DEBUG
app.config['SECRET_KEY'] = config['SECRET_KEY']

# Register the blueprints
app.register_blueprint(movie_bp)
app.register_blueprint(event_bp)
app.register_blueprint(user_bp)
app.register_blueprint(theater_bp)
app.register_blueprint(booking_bp)

if __name__ == '__main__':
    app.run()
