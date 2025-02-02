from flask_restful import Resource, request
from package.models import db, Appointment  

class Appointments(Resource):
    """This contains APIs to carry out activities with all appointments"""

    def get(self):
        """Retrieve all appointments and return in the form of JSON"""
        appointments = Appointment.query.all()  # Get all appointments from the database
        return [appointment.to_dict() for appointment in appointments], 200

    def post(self):
        """Create an appointment by associating patient and doctor with appointment date"""
        appointment_data = request.get_json(force=True)
        new_appointment = Appointment(
            pat_id=appointment_data['pat_id'],
            doc_id=appointment_data['doc_id'],
            appointment_date=appointment_data['appointment_date']
        )
        db.session.add(new_appointment)
        db.session.commit()
        return new_appointment.to_dict(), 201  # Return the newly created appointment


class AppointmentResource(Resource):
    """This contains all APIs for managing a single appointment"""

    def get(self, id):
        """Retrieve a single appointment's details by its id"""
        appointment = Appointment.query.filter_by(app_id=id).first()  # Get appointment by ID
        if appointment:
            return appointment.to_dict(), 200
        return {'msg': 'Appointment not found'}, 404

    def put(self, id):
        """Update the appointment details by the appointment id"""
        appointment = Appointment.query.filter_by(app_id=id).first()
        if not appointment:
            return {'msg': 'Appointment not found'}, 404

        appointment_data = request.get_json(force=True)
        appointment.pat_id = appointment_data['pat_id']
        appointment.doc_id = appointment_data['doc_id']
        appointment.appointment_date = appointment_data['appointment_date']
        
        db.session.commit()
        return appointment.to_dict(), 200

    def delete(self, id):
        """Delete the appointment by its id"""
        appointment = Appointment.query.filter_by(app_id=id).first()
        if not appointment:
            return {'msg': 'Appointment not found'}, 404

        db.session.delete(appointment)
        db.session.commit()
        return {'msg': 'Successfully deleted'}, 200
