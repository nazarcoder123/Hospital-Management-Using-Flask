# package/patient.py
import logging
from flask_restful import Resource, request
from package.models import db, Patient  # Import from package.models

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Patients(Resource):
    """Contains all APIs for activities with multiple patients."""
    def get(self):
        logger.debug("Starting GET /patients to retrieve all patients")
        try:
            patients = Patient.query.order_by(Patient.pat_date.desc()).all()
            patients_list = [patient.to_dict() for patient in patients]
            logger.debug("Fetched patients: %s", patients_list)
            return patients_list, 200
        except Exception as e:
            logger.error("Error retrieving patients: %s", e)
            return {"error": "Could not retrieve patients"}, 500

    def post(self):
        logger.debug("Starting POST /patients to add a new patient")
        try:
            patientInput = request.get_json(force=True)
            logger.debug("Received patient input: %s", patientInput)
            new_patient = Patient(
                pat_first_name=patientInput['pat_first_name'],
                pat_last_name=patientInput['pat_last_name'],
                pat_insurance_no=patientInput['pat_insurance_no'],
                pat_ph_no=patientInput['pat_ph_no'],
                pat_address=patientInput['pat_address']
            )
            db.session.add(new_patient)
            db.session.commit()
            logger.debug("Inserted patient with ID: %s", new_patient.pat_id)
            return new_patient.to_dict(), 201
        except Exception as e:
            logger.error("Error adding new patient: %s", e)
            db.session.rollback()
            return {"error": "Could not add patient"}, 500

class PatientResource(Resource):
    """Contains all APIs for activities with a single patient entity."""
    def get(self, id):
        logger.debug("Starting GET /patient/%s to retrieve patient details", id)
        try:
            patient = Patient.query.get(id)
            if not patient:
                logger.warning("Patient with ID %s not found", id)
                return {"error": "Patient not found"}, 404
            logger.debug("Fetched patient: %s", patient.to_dict())
            return patient.to_dict(), 200
        except Exception as e:
            logger.error("Error retrieving patient with ID %s: %s", id, e)
            return {"error": "Could not retrieve patient"}, 500

    def delete(self, id):
        logger.debug("Starting DELETE /patient/%s", id)
        try:
            patient = Patient.query.get(id)
            if not patient:
                logger.warning("Patient with ID %s not found for deletion", id)
                return {"error": "Patient not found"}, 404
            db.session.delete(patient)
            db.session.commit()
            logger.debug("Deleted patient with ID: %s", id)
            return {'msg': 'successfully deleted'}, 200
        except Exception as e:
            logger.error("Error deleting patient with ID %s: %s", id, e)
            db.session.rollback()
            return {"error": "Could not delete patient"}, 500

    def put(self, id):
        logger.debug("Starting PUT /patient/%s to update patient details", id)
        try:
            patientInput = request.get_json(force=True)
            logger.debug("Received update input for patient ID %s: %s", id, patientInput)
            patient = Patient.query.get(id)
            if not patient:
                logger.warning("Patient with ID %s not found for update", id)
                return {"error": "Patient not found"}, 404
            patient.pat_first_name = patientInput['pat_first_name']
            patient.pat_last_name = patientInput['pat_last_name']
            patient.pat_insurance_no = patientInput['pat_insurance_no']
            patient.pat_ph_no = patientInput['pat_ph_no']
            patient.pat_address = patientInput['pat_address']
            db.session.commit()
            logger.debug("Updated patient with ID: %s", id)
            return patient.to_dict(), 200
        except Exception as e:
            logger.error("Error updating patient with ID %s: %s", id, e)
            db.session.rollback()
            return {"error": "Could not update patient"}, 500
