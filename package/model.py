import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Load configuration from file
with open('config.json') as f:
    config = json.load(f)

# Create a Flask application instance
app = Flask(__name__)

# Configure the SQLAlchemy connection string for PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{config['user']}:{config['password']}@"
    f"{config['host']}/{config['database']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM instance
db = SQLAlchemy(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()