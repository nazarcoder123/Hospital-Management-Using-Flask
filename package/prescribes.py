from flask_restful import Resource, request
from package.models import db, Prescribe  # Assuming `db` is your SQLAlchemy instance and Prescribe is the model


class Prescribes(Resource):
    """This contains APIs to carry out activity with all prescriptions"""

    def get(self):
        """Retrieve all prescriptions and return in the form of JSON"""
        prescribes = Prescribe.query.all()  # Get all prescriptions
        return [prescribe.to_dict() for prescribe in prescribes], 200

    def post(self):
        """API to add a prescription in the database"""
        prescribe_data = request.get_json(force=True)

        new_prescribe = Prescribe(
            doc_id=prescribe_data['doc_id'],
            pat_id=prescribe_data['pat_id'],
            med_code=prescribe_data['med_code'],
            p_date=prescribe_data['p_date'],
            app_id=prescribe_data['app_id'],
            dose=prescribe_data['dose']
        )

        db.session.add(new_prescribe)
        db.session.commit()

        return new_prescribe.to_dict(), 201  # Return the newly created prescription data


class PrescribeResource(Resource):
    """This contains all APIs for managing a single prescription"""

    def get(self, doc_id):
        """Retrieve a single prescription's details by its doc_id"""
        prescribe = Prescribe.query.filter_by(doc_id=doc_id).first()  # Get prescription by doc_id
        if prescribe:
            return prescribe.to_dict(), 200
        return {'msg': 'Prescription not found'}, 404

    def put(self, doc_id):
        """Update a prescription's details by the doc_id"""
        prescribe = Prescribe.query.filter_by(doc_id=doc_id).first()

        if not prescribe:
            return {'msg': 'Prescription not found'}, 404

        prescribe_data = request.get_json(force=True)

        prescribe.doc_id = prescribe_data['doc_id']
        prescribe.pat_id = prescribe_data['pat_id']
        prescribe.med_code = prescribe_data['med_code']
        prescribe.p_date = prescribe_data['p_date']
        prescribe.app_id = prescribe_data['app_id']
        prescribe.dose = prescribe_data['dose']

        db.session.commit()

        return prescribe.to_dict(), 200

    def delete(self, doc_id):
        """Delete a prescription by its doc_id"""
        prescribe = Prescribe.query.filter_by(doc_id=doc_id).first()

        if not prescribe:
            return {'msg': 'Prescription not found'}, 404

        db.session.delete(prescribe)
        db.session.commit()

        return {'msg': 'Successfully deleted'}, 200
