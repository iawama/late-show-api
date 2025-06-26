from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from models import Guest, Episode, Appearance, User
from controllers import auth_controller, guest_controller, episode_controller, appearance_controller

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_controller.bp)
app.register_blueprint(guest_controller.bp)
app.register_blueprint(episode_controller.bp)
app.register_blueprint(appearance_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)