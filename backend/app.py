# # app.py

# from flask import Flask
# from config import MONGO_URI
# from routes.movie_routes import movie_bp
# from routes.event_routes import event_bp
# from routes.user_routes import user_bp
# from routes.theater_routes import theater_bp
# from routes.booking_routes import booking_bp

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'my-secret-key'

# # Register the blueprints
# app.register_blueprint(movie_bp)
# app.register_blueprint(event_bp)
# app.register_blueprint(user_bp)
# app.register_blueprint(theater_bp)
# app.register_blueprint(booking_bp)

# if __name__ == '__main__':
#     app.run()

# app.py
from flask import Flask
from routes.movie_routes import movie_bp
from routes.event_routes import event_bp
from routes.user_routes import user_bp
from routes.theater_routes import theater_bp
from routes.booking_routes import booking_bp
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)

# Other configurations

# Register the blueprints
app.register_blueprint(movie_bp)
app.register_blueprint(event_bp)
app.register_blueprint(user_bp)
app.register_blueprint(theater_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run()
