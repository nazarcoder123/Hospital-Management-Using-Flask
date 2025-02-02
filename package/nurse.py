# from flask_restful import Resource, request
# from package.models import db, Nurse

# class Nurses(Resource):
#     """API to manage all nurses"""

#     def get(self):
#         """Retrieve list of all nurses"""
#         nurses = Nurse.query.order_by(Nurse.nur_date.desc()).all()
#         return [nurse.__dict__ for nurse in nurses]

#     def post(self):
#         """Add a new nurse"""
#         nurseInput = request.get_json(force=True)
#         new_nurse = Nurse(
#             nur_first_name=nurseInput['nur_first_name'],
#             nur_last_name=nurseInput['nur_last_name'],
#             nur_ph_no=nurseInput['nur_ph_no'],
#             nur_address=nurseInput['nur_address']
#         )
#         db.session.add(new_nurse)
#         db.session.commit()
#         return nurseInput
    
    

# class NurseResource(Resource):
#     """API to manage a single nurse"""

#     def get(self, id):
#         """Retrieve nurse by ID"""
#         nurse = Nurse.query.get(id)
#         return nurse.__dict__ if nurse else {'msg': 'Nurse not found'}

#     def delete(self, id):
#         """Delete nurse by ID"""
#         nurse = Nurse.query.get(id)
#         if nurse:
#             db.session.delete(nurse)
#             db.session.commit()
#             return {'msg': 'Successfully deleted'}
#         return {'msg': 'Nurse not found'}

#     def put(self, id):
#         """Update nurse by ID"""
#         nurse = Nurse.query.get(id)
#         if not nurse:
#             return {'msg': 'Nurse not found'}

#         nurseInput = request.get_json(force=True)
#         nurse.nur_first_name = nurseInput['nur_first_name']
#         nurse.nur_last_name = nurseInput['nur_last_name']
#         nurse.nur_ph_no = nurseInput['nur_ph_no']
#         nurse.nur_address = nurseInput['nur_address']

#         db.session.commit()
#         return nurseInput



from flask_restful import Resource, request
from package.models import db, Nurse

class Nurses(Resource):
    """API to manage all nurses"""

    def get(self):
        """Retrieve list of all nurses"""
        nurses = Nurse.query.order_by(Nurse.nur_date.desc()).all()
        return [nurse.to_dict() for nurse in nurses], 200  # Use to_dict()

    def post(self):
        """Add a new nurse"""
        nurseInput = request.get_json(force=True)
        new_nurse = Nurse(
            nur_first_name=nurseInput['nur_first_name'],
            nur_last_name=nurseInput['nur_last_name'],
            nur_ph_no=nurseInput['nur_ph_no'],
            nur_address=nurseInput['nur_address']
        )
        db.session.add(new_nurse)
        db.session.commit()
        return nurseInput
    
    

class NurseResource(Resource):
    """API to manage a single nurse"""

    def get(self, id):
        """Retrieve nurse by ID"""
        nurse = Nurse.query.get(id)
        return nurse.to_dict() if nurse else {'msg': 'Nurse not found'}, 404

    def delete(self, id):
        """Delete nurse by ID"""
        nurse = Nurse.query.get(id)
        if nurse:
            db.session.delete(nurse)
            db.session.commit()
            return {'msg': 'Successfully deleted'}
        return {'msg': 'Nurse not found'}

    def put(self, id):
        """Update nurse by ID"""
        nurse = Nurse.query.get(id)
        if not nurse:
            return {'msg': 'Nurse not found'}

        nurseInput = request.get_json(force=True)
        nurse.nur_first_name = nurseInput['nur_first_name']
        nurse.nur_last_name = nurseInput['nur_last_name']
        nurse.nur_ph_no = nurseInput['nur_ph_no']
        nurse.nur_address = nurseInput['nur_address']

        db.session.commit()
        return nurseInput
