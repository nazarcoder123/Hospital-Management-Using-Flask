import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Load configuration from file
with open('config.json') as f:
    config = json.load(f)

app = Flask(__name__)

# Configure the SQLAlchemy connection string for PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{config['user']}:{config['password']}@"
    f"{config['host']}/{config['database']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import your models (which should use the same db instance)
from package.models import db  # This is the instance created in models.py

# Initialize the SQLAlchemy instance with the app
db.init_app(app)

# Optionally, create all tables if running as a script (use Flask-Migrate for production)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()