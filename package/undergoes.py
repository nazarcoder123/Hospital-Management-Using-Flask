from flask_restful import Resource, request
from package.models import db, Undergoes

class UndergoesList(Resource):
    """APIs for all undergoes records"""

    def get(self):
        """Retrieve all undergoes records"""
        undergoes_records = Undergoes.query.all()
        return [record.to_dict() for record in undergoes_records], 200

    def post(self):
        """Add a new undergoes record"""
        undergoes_data = request.get_json(force=True)

        new_undergoes = Undergoes(
            pat_id=undergoes_data['pat_id'],
            proc_code=undergoes_data['proc_code'],
            u_date=undergoes_data['u_date'],
            doc_id=undergoes_data['doc_id'],
            nur_id=undergoes_data['nur_id'],
            room_no=undergoes_data['room_no']
        )

        db.session.add(new_undergoes)
        db.session.commit()
        return new_undergoes.to_dict(), 201


class UndergoesResource(Resource):
    """APIs for single undergoes record"""

    def get(self, pat_id):
        """Retrieve a single undergoes record by pat_id"""
        undergoes = Undergoes.query.filter_by(pat_id=pat_id).first()
        if undergoes:
            return undergoes.to_dict(), 200
        return {'msg': 'Undergoes record not found'}, 404

    def put(self, pat_id):
        """Update an undergoes record"""
        undergoes = Undergoes.query.filter_by(pat_id=pat_id).first()
        if not undergoes:
            return {'msg': 'Undergoes record not found'}, 404

        undergoes_data = request.get_json(force=True)
        undergoes.proc_code = undergoes_data['proc_code']
        undergoes.u_date = undergoes_data['u_date']
        undergoes.doc_id = undergoes_data['doc_id']
        undergoes.nur_id = undergoes_data['nur_id']
        undergoes.room_no = undergoes_data['room_no']

        db.session.commit()
        return undergoes.to_dict(), 200

    def delete(self, pat_id):
        """Delete an undergoes record"""
        undergoes = Undergoes.query.filter_by(pat_id=pat_id).first()
        if not undergoes:
            return {'msg': 'Undergoes record not found'}, 404

        db.session.delete(undergoes)
        db.session.commit()
        return {'msg': 'Successfully deleted'}, 200
