from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "last.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import Student, Job, Employee  # Import models here

    # Register blueprints
    app.register_blueprint(views)
    app.register_blueprint(auth)

    # Create database tables
    with app.app_context():
        db.create_all()
        print("Database created!")

    # Initialize LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Set the login view for unauthorized users
    login_manager.init_app(app)

    # User loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        # Load the user from the Student or Employee class based on the user_id
        return Student.query.get(user_id) or Employee.query.get(user_id)

    return app




