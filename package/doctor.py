# package/doctor.py
import logging
from flask_restful import Resource, request
from package.models import db, Doctor  # Import the central db and Doctor model

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Doctors(Resource):
    """Contains APIs to carry out activity with all doctors."""
    
    def get(self):
        """Retrieve list of all doctors, ordered by doc_date descending."""
        logger.debug("Starting GET /doctor to retrieve all doctors")
        try:
            doctors = Doctor.query.order_by(Doctor.doc_date.desc()).all()
            doctors_list = [doctor.to_dict() for doctor in doctors]
            logger.debug("Fetched doctors: %s", doctors_list)
            return doctors_list, 200
        except Exception as e:
            logger.error("Error retrieving doctors: %s", e)
            return {"error": "Could not retrieve doctors"}, 500

    def post(self):
        """Add a new doctor."""
        logger.debug("Starting POST /doctor to add a new doctor")
        try:
            doctorInput = request.get_json(force=True)
            logger.debug("Received doctor input: %s", doctorInput)
            new_doctor = Doctor(
                doc_first_name=doctorInput['doc_first_name'],
                doc_last_name=doctorInput['doc_last_name'],
                doc_ph_no=doctorInput['doc_ph_no'],
                doc_address=doctorInput['doc_address']
            )
            db.session.add(new_doctor)
            db.session.commit()
            logger.debug("Inserted doctor with ID: %s", new_doctor.doc_id)
            return new_doctor.to_dict(), 201
        except Exception as e:
            logger.error("Error adding new doctor: %s", e)
            db.session.rollback()
            return {"error": "Could not add doctor"}, 500

class DoctorResource(Resource):
    """Includes APIs to perform actions with a single doctor."""
    
    def get(self, id):
        """Retrieve details of the doctor by doctor id."""
        logger.debug("Starting GET /doctor/%s to retrieve doctor details", id)
        try:
            doctor = Doctor.query.get(id)
            if not doctor:
                logger.warning("Doctor with ID %s not found", id)
                return {"error": "Doctor not found"}, 404
            logger.debug("Fetched doctor: %s", doctor.to_dict())
            return doctor.to_dict(), 200
        except Exception as e:
            logger.error("Error retrieving doctor with ID %s: %s", id, e)
            return {"error": "Could not retrieve doctor"}, 500

    def delete(self, id):
        """Delete the doctor by its id."""
        logger.debug("Starting DELETE /doctor/%s", id)
        try:
            doctor = Doctor.query.get(id)
            if not doctor:
                logger.warning("Doctor with ID %s not found for deletion", id)
                return {"error": "Doctor not found"}, 404
            db.session.delete(doctor)
            db.session.commit()
            logger.debug("Deleted doctor with ID: %s", id)
            return {"msg": "successfully deleted"}, 200
        except Exception as e:
            logger.error("Error deleting doctor with ID %s: %s", id, e)
            db.session.rollback()
            return {"error": "Could not delete doctor"}, 500

    def put(self, id):
        """Update the doctor by its id."""
        logger.debug("Starting PUT /doctor/%s to update doctor details", id)
        try:
            doctorInput = request.get_json(force=True)
            logger.debug("Received update input for doctor ID %s: %s", id, doctorInput)
            doctor = Doctor.query.get(id)
            if not doctor:
                logger.warning("Doctor with ID %s not found for update", id)
                return {"error": "Doctor not found"}, 404
            # Update doctor fields
            doctor.doc_first_name = doctorInput['doc_first_name']
            doctor.doc_last_name = doctorInput['doc_last_name']
            doctor.doc_ph_no = doctorInput['doc_ph_no']
            doctor.doc_address = doctorInput['doc_address']
            db.session.commit()
            logger.debug("Updated doctor with ID: %s", id)
            return doctor.to_dict(), 200
        except Exception as e:
            logger.error("Error updating doctor with ID %s: %s", id, e)
            db.session.rollback()
            return {"error": "Could not update doctor"}, 500
