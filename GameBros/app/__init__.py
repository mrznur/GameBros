from flask import Flask
from app.controllers.auth_controller import auth_bp
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'
    app.config['UPLOAD_FOLDER'] = 'app/static/img'
    app.config['DATABASE'] = os.path.join('instance', 'database.db')

    app.register_blueprint(auth_bp)

    return app
