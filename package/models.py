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
    
    room_no = db.Column(db.String(50), primary_key=True,autoincrement=True)
    room_type = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        """Convert Room object to dictionary."""
        return {
            "room_no": self.room_no,
            "room_type": self.room_type,
            "available": self.available
        }