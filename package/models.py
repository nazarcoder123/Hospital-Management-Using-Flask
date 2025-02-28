from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create the SQLAlchemy instance without the app
db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patient'
    
    pat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pat_first_name = db.Column(db.String(50), nullable=False)
    pat_last_name = db.Column(db.String(50), nullable=False)
    pat_insurance_no = db.Column(db.String(50), nullable=False)
    pat_ph_no = db.Column(db.String(20), nullable=False)
    pat_address = db.Column(db.String(200), nullable=False)
    pat_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'pat_id': self.pat_id,
            'pat_first_name': self.pat_first_name,
            'pat_last_name': self.pat_last_name,
            'pat_insurance_no': self.pat_insurance_no,
            'pat_ph_no': self.pat_ph_no,
            'pat_address': self.pat_address,
            'pat_date': self.pat_date.isoformat() if self.pat_date else None,
        }

class Doctor(db.Model):
    __tablename__ = 'doctor'
    
    doc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doc_first_name = db.Column(db.String(50), nullable=False)
    doc_last_name = db.Column(db.String(50), nullable=False)
    doc_ph_no = db.Column(db.String(20), nullable=False)
    doc_address = db.Column(db.String(200), nullable=False)
    doc_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'doc_id': self.doc_id,
            'doc_first_name': self.doc_first_name,
            'doc_last_name': self.doc_last_name,
            'doc_ph_no': self.doc_ph_no,
            'doc_address': self.doc_address,
            'doc_date': self.doc_date.isoformat() if self.doc_date else None,
        }

class Nurse(db.Model):
    __tablename__ = 'nurse'
    nur_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nur_first_name = db.Column(db.String(100), nullable=False)
    nur_last_name = db.Column(db.String(100), nullable=False)
    nur_ph_no = db.Column(db.String(15), nullable=False)
    nur_address = db.Column(db.String(255), nullable=False)
    nur_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "nur_id": self.nur_id,
            "nur_first_name": self.nur_first_name,
            "nur_last_name": self.nur_last_name,
            "nur_ph_no": self.nur_ph_no,
            "nur_address": self.nur_address,
            "nur_date": self.nur_date.strftime("%Y-%m-%d %H:%M:%S") if self.nur_date else None
        }

class Department(db.Model):
    __tablename__ = 'department'
    
    # If you want auto-increment, set autoincrement=True
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(80), nullable=False)
    head_id = db.Column(db.Integer, db.ForeignKey('doctor.doc_id'), nullable=False)
    
    # Relationship to access the head doctor directly
    head = db.relationship('Doctor', backref='managed_departments')

    def to_dict(self):
        return {
            "department_id": self.department_id,
            "name": self.name,
            "head_id": self.head_id,
            "head_name": f"{self.head.doc_first_name} {self.head.doc_last_name}" if self.head else None
        }

class Room(db.Model):
    __tablename__ = 'room'
    
    # If you want auto-increment, set autoincrement=True
    room_no = db.Column(db.Integer, primary_key=True, autoincrement=False)
    room_type = db.Column(db.String(50), nullable=False)
    # Change this to Boolean if you prefer
    available = db.Column(db.Integer, nullable=False, default=True)

    def __repr__(self):
        return f'<Room {self.room_no} - {self.room_type}>'

    def to_dict(self):
        return {
            "room_no": self.room_no,
            "room_type": self.room_type,
            "available": self.available
        }

class Appointment(db.Model):
    __tablename__ = 'appointment'

    # If you truly want auto-increment, set autoincrement=True
    app_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pat_id = db.Column(db.Integer, db.ForeignKey('patient.pat_id'), nullable=False)
    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.doc_id'), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)

    # Relationships
    patient = db.relationship('Patient', backref='appointments', lazy=True)
    doctor = db.relationship('Doctor', backref='appointments', lazy=True)

    def to_dict(self):
        return {
            "app_id": self.app_id,
            "pat_id": self.pat_id,
            "doc_id": self.doc_id,
            "appointment_date": self.appointment_date.strftime('%Y-%m-%d')
                if self.appointment_date else None,
            "pat_id": self.pat_id,
            # Instead of "patient_name", return pat_first_name & pat_last_name
            "pat_first_name": self.patient.pat_first_name if self.patient else None,
            "pat_last_name": self.patient.pat_last_name if self.patient else None,

            "doc_id": self.doc_id,
            # Instead of "doctor_name", return doc_first_name & doc_last_name
            "doc_first_name": self.doctor.doc_first_name if self.doctor else None,
            "doc_last_name": self.doctor.doc_last_name if self.doctor else None,
        }

class Medication(db.Model):
    __tablename__ = 'medication'

    code = db.Column(db.String(50), primary_key=True)  # code is unique
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "brand": self.brand,
            "description": self.description
        }

class Procedure(db.Model):
    __tablename__ = 'procedure'

    code = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "cost": self.cost
        }

class Prescribe(db.Model):
    __tablename__ = 'prescribes'

    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.doc_id'), primary_key=True)
    pat_id = db.Column(db.Integer, db.ForeignKey('patient.pat_id'), primary_key=True)
    med_code = db.Column(db.String(100), nullable=False)
    p_date = db.Column(db.Date, nullable=False)
    app_id = db.Column(db.Integer, db.ForeignKey('appointment.app_id'), nullable=False)
    dose = db.Column(db.String(100), nullable=False)

    # Relationships
    doctor = db.relationship('Doctor', backref='prescriptions', lazy=True)
    patient = db.relationship('Patient', backref='prescriptions', lazy=True)
    appointment = db.relationship('Appointment', backref='prescriptions', lazy=True)

    # def to_dict(self):
    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "doc_first_name": self.doctor.doc_first_name if self.doctor else None,
            "doc_last_name": self.doctor.doc_last_name if self.doctor else None,
            "pat_id": self.pat_id,
            "pat_first_name": self.patient.pat_first_name if self.patient else None,
            "pat_last_name": self.patient.pat_last_name if self.patient else None,
            "med_code": self.med_code,
            "p_date": self.p_date.isoformat() if self.p_date else None,
            "app_id": self.app_id,
            "dose": self.dose
    }

class Undergoes(db.Model):
    __tablename__ = 'undergoes'

    pat_id = db.Column(db.Integer, db.ForeignKey('patient.pat_id'), primary_key=True)
    proc_code = db.Column(db.String(50), db.ForeignKey('procedure.code'), nullable=False)
    u_date = db.Column(db.Date, nullable=False)
    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.doc_id'), nullable=False)
    nur_id = db.Column(db.Integer, db.ForeignKey('nurse.nur_id'), nullable=False)
    room_no = db.Column(db.Integer, nullable=False)

    # Relationships
    patient = db.relationship('Patient', backref='undergoes')
    doctor = db.relationship('Doctor', backref='undergoes')
    nurse = db.relationship('Nurse', backref='undergoes')
    procedure = db.relationship('Procedure', backref='undergoes')

    def to_dict(self):
        return {
            "pat_id": self.pat_id,
            # Instead of "patient_name", return pat_first_name & pat_last_name
            "pat_first_name": self.patient.pat_first_name if self.patient else None,
            "pat_last_name": self.patient.pat_last_name if self.patient else None,

            "proc_code": self.proc_code,
            "procedure_name": self.procedure.name if self.procedure else None,
            "u_date": self.u_date.strftime('%Y-%m-%d') if self.u_date else None,

            "doc_id": self.doc_id,
            # Instead of "doctor_name", return doc_first_name & doc_last_name
            "doc_first_name": self.doctor.doc_first_name if self.doctor else None,
            "doc_last_name": self.doctor.doc_last_name if self.doctor else None,

            "nur_id": self.nur_id,
            # If your table wants nurse_first_name / nurse_last_name:
            "nur_first_name": self.nurse.nur_first_name if self.nurse else None,
            "nur_last_name": self.nurse.nur_last_name if self.nurse else None,

            "room_no": self.room_no
    }
