"""from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

from app import db, create_app
#from app.models import User  # or wherever your User model is defined

app = create_app()

with app.app_context():
    db.create_all()
    
    # Optional: Add a test user\
    if not User.query.filter_by(email="test@example.com").first():
        new_user = User(email="test@example.com", password="hashed_password")
        db.session.add(new_user)
        db.session.commit()

    print(" Database created with a sample user.")"""
from app import create_app
from app.db import init_db, create_test_user
from app.model_loader import load_models

app = create_app()

def startup_tasks():
    init_db(app)
    create_test_user(app)
    load_models("app/models")     # heavy model loading
    print("🚀 Startup tasks completed. Server running...")

if __name__ == "__main__":
    startup_tasks()
    app.run(host="0.0.0.0", port=8080)
