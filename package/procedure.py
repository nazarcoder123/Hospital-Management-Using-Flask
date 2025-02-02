from flask_restful import Resource, request
from package.models import db, Procedure

class Procedures(Resource):
    """This contains APIs to manage all procedures"""

    def get(self):
        """Retrieve all procedures and return them as JSON"""
        procedures = Procedure.query.all()  # ORM query to get all procedures
        return [proc.to_dict() for proc in procedures], 200

    def post(self):
        """API to add a new procedure to the database"""
        procedure_data = request.get_json(force=True)

        new_procedure = Procedure(
            code=procedure_data['code'],
            name=procedure_data['name'],
            cost=procedure_data['cost']
        )
        
        db.session.add(new_procedure)
        db.session.commit()
        return new_procedure.to_dict(), 201


class ProcedureResource(Resource):
    """This contains APIs for managing a single procedure"""

    def get(self, code):
        """Retrieve a single procedure by its code"""
        procedure = Procedure.query.filter_by(code=code).first()
        if procedure:
            return procedure.to_dict(), 200
        return {'msg': 'Procedure not found'}, 404

    def put(self, code):
        """Update the procedure details by its code"""
        procedure = Procedure.query.filter_by(code=code).first()
        if not procedure:
            return {'msg': 'Procedure not found'}, 404

        procedure_data = request.get_json(force=True)
        procedure.name = procedure_data['name']
        procedure.cost = procedure_data['cost']

        db.session.commit()
        return procedure.to_dict(), 200

    def delete(self, code):
        """Delete the procedure by its code"""
        procedure = Procedure.query.filter_by(code=code).first()
        if not procedure:
            return {'msg': 'Procedure not found'}, 404

        db.session.delete(procedure)
        db.session.commit()
        return {'msg': 'Successfully deleted'}, 200
