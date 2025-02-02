from flask_restful import Resource, request
from package.models import db, Medication

class Medications(Resource):
    """This contains APIs to manage all medications"""

    def get(self):
        """Retrieve all medications and return them as JSON"""
        medications = Medication.query.all()  # ORM query to get all medications
        return [med.to_dict() for med in medications], 200

    def post(self):
        """API to add a new medication to the database"""
        medication_data = request.get_json(force=True)

        new_medication = Medication(
            code=medication_data['code'],
            name=medication_data['name'],
            brand=medication_data['brand'],
            description=medication_data.get('description', '')  # Default to empty string if missing
        )
        
        db.session.add(new_medication)
        db.session.commit()
        return new_medication.to_dict(), 201


class MedicationResource(Resource):
    """This contains APIs for managing a single medication"""

    def get(self, code):
        """Retrieve a single medication by its code"""
        medication = Medication.query.filter_by(code=code).first()
        if medication:
            return medication.to_dict(), 200
        return {'msg': 'Medication not found'}, 404

    def put(self, code):
        """Update the medication details by its code"""
        medication = Medication.query.filter_by(code=code).first()
        if not medication:
            return {'msg': 'Medication not found'}, 404

        medication_data = request.get_json(force=True)
        medication.name = medication_data['name']
        medication.brand = medication_data['brand']
        medication.description = medication_data['description']

        db.session.commit()
        return medication.to_dict(), 200

    def delete(self, code):
        """Delete the medication by its code"""
        medication = Medication.query.filter_by(code=code).first()
        if not medication:
            return {'msg': 'Medication not found'}, 404

        db.session.delete(medication)
        db.session.commit()
        return {'msg': 'Successfully deleted'}, 200
