"""from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 

db = SQLAlchemy() 
login_manager = LoginManager() 

def create_app():
     
  app = Flask(__name__) 
  app.config['SECRET_KEY'] = 'demo-secret-key' 
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' 
  
  db.init_app(app) 
  login_manager.init_app(app) 
  login_manager.login_view = 'auth.login' 
  # Import and register blueprints 
  from .routes import main as main_blueprint 
  app.register_blueprint(main_blueprint) 
  
  from .auth import auth as auth_blueprint 
  app.register_blueprint(auth_blueprint) 
  return app"""
  
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # --- FIX: ALWAYS PUT SQLITE DB INSIDE INSTANCE FOLDER ---
    instance_path = os.path.join(app.root_path, '..', 'instance')
    os.makedirs(instance_path, exist_ok=True)
    db_path = os.path.join(instance_path, 'users.db')

    app.config['SECRET_KEY'] = 'demo-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .routes import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
