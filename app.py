from flask import Flask
from config import Config
from models.models import db, User
from routes.auth import auth_bp, create_admin_user
from routes.dashboard import dashboard_bp
from routes.tugas import tugas_bp
from routes.anggota import anggota_bp
from flask_login import LoginManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Silakan login untuk mengakses halaman ini.'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(tugas_bp)
    app.register_blueprint(anggota_bp)

    # Create tables and admin user
    with app.app_context():
        db.create_all()
        create_admin_user()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)