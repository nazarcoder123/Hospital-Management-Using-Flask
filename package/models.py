# package/models.py
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

## The below code is for doctor

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
        """Convert Nurse object to dictionary."""
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
    
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(80), nullable=False)
    head_id = db.Column(db.Integer, db.ForeignKey('doctor.doc_id'), nullable=False)
    
    # Relationship to access the head doctor directly
    head = db.relationship('Doctor', backref='managed_departments')
        

class Room(db.Model):
    __tablename__ = 'room'
    
    room_no = db.Column(db.Integer, primary_key=True, autoincrement=False)
    room_type = db.Column(db.String(50), nullable=False)
    available = db.Column(db.Integer, nullable=False, default=True)

    def __repr__(self):
        return f'<Room {self.room_no} - {self.room_type}>'
    


class Prescribe(db.Model):
    __tablename__ = 'prescribes'

    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.doc_id'), primary_key=True)
    pat_id = db.Column(db.Integer, db.ForeignKey('patient.pat_id'), primary_key=True)
    med_code = db.Column(db.String(100), nullable=False)
    p_date = db.Column(db.Date, nullable=False)
    app_id = db.Column(db.Integer, db.ForeignKey('appointment.app_id'), nullable=False)
    dose = db.Column(db.String(100), nullable=False)

    # Relationship with Doctor, Patient, and Appointment
    doctor = db.relationship('Doctor', backref='prescriptions', lazy=True)
    patient = db.relationship('Patient', backref='prescriptions', lazy=True)
    appointment = db.relationship('Appointment', backref='prescriptions', lazy=True)

    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "doctor_name": f"{self.doctor.doc_first_name} {self.doctor.doc_last_name}",
            "pat_id": self.pat_id,
            "patient_name": f"{self.patient.pat_first_name} {self.patient.pat_last_name}",
            "med_code": self.med_code,
            "p_date": self.p_date.isoformat(),  # Date in ISO format (yyyy-mm-dd)
            "app_id": self.app_id,
            "dose": self.dose
        }


class Appointment(db.Model):
    __tablename__ = 'appointment'

    app_id = db.Column(db.Integer, primary_key=True)  # Assuming auto-incremented here
    pat_id = db.Column(db.Integer, db.ForeignKey('patient.pat_id'), nullable=False)
    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.doc_id'), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)

    # Relationships
    patient = db.relationship('Patient', backref='appointments', lazy=True)
    doctor = db.relationship('Doctor', backref='appointments', lazy=True)

    def to_dict(self):
        """Convert Appointment object to dictionary"""
        return {
            "app_id": self.app_id,
            "pat_id": self.pat_id,
            "doc_id": self.doc_id,
            "appointment_date": self.appointment_date.strftime('%Y-%m-%d'),
            "patient_name": f"{self.patient.pat_first_name} {self.patient.pat_last_name}",
            "doctor_name": f"{self.doctor.doc_first_name} {self.doctor.doc_last_name}"
        }

class Medication(db.Model):
    __tablename__ = 'medication'

    code = db.Column(db.String(50), primary_key=True)  # Assuming code is unique
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert Medication object to dictionary"""
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
        """Convert Procedure object to dictionary"""
        return {
            "code": self.code,
            "name": self.name,
            "cost": self.cost
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
        """Convert Undergoes object to dictionary"""
        return {
            "pat_id": self.pat_id,
            "patient_name": f"{self.patient.pat_first_name} {self.patient.pat_last_name}",
            "proc_code": self.proc_code,
            "procedure_name": self.procedure.name,
            "u_date": self.u_date.strftime('%Y-%m-%d'),
            "doc_id": self.doc_id,
            "doctor_name": f"{self.doctor.doc_first_name} {self.doctor.doc_last_name}",
            "nur_id": self.nur_id,
            "nurse_name": f"{self.nurse.nur_first_name} {self.nurse.nur_last_name}",
            "room_no": self.room_no
        }
