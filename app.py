import json
from flask import Flask, send_from_directory
from flask_restful import Api
from package.patient import Patients, PatientResource
from package.doctor import Doctors, DoctorResource
from package.nurse import Nurses, NurseResource
from package.department import Departments, DepartmentResource
from package.room import Rooms, RoomResource  
from package.models import db  
import os

# Load configuration from file
with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')

# Configure the SQLAlchemy connection string for PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance with the app
db.init_app(app)

api = Api(app)

# Add resources for Patients, Doctors, Nurses, Departments, and Rooms
api.add_resource(Patients, '/patient')
api.add_resource(PatientResource, '/patient/<int:id>')
api.add_resource(Doctors, '/doctor')
api.add_resource(DoctorResource, '/doctor/<int:id>')
api.add_resource(Nurses, '/nurse')
api.add_resource(NurseResource, '/nurse/<int:id>')
api.add_resource(Departments, '/department')
api.add_resource(DepartmentResource, '/department/<int:department_id>')
api.add_resource(Rooms, '/rooms')  
api.add_resource(RoomResource, '/room/<string:room_no>')  

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create all tables if they don't exist yet
    app.run(debug=True, host=config['host'], port=config['port'])
