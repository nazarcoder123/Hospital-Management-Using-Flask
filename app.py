# app.py
import json
from flask import Flask, send_from_directory
from flask_restful import Api
from package.patient import Patients, PatientResource  # your resource classes
from package.models import db  # Import the db instance
import os

with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance with the app
db.init_app(app)

api = Api(app)
api.add_resource(Patients, '/patient')
api.add_resource(PatientResource, '/patient/<int:id>')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    # Create the tables if they don't exist. This must be run within an app context.
    with app.app_context():
        db.create_all()
    app.run(debug=True, host=config['host'], port=config['port'])
