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
        