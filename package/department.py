from flask_restful import Resource, request
from package.models import db, Department, Doctor

class Departments(Resource):
    """APIs for multiple departments"""
    
    def get(self):
        departments = Department.query.all()
        departments_data = []
        for dept in departments:
            departments_data.append({
                'department_id': dept.department_id,
                'name': dept.name,
                'head_id': dept.head_id,
                'doc_first_name': dept.head.doc_first_name,
                'doc_last_name': dept.head.doc_last_name
            })
        return departments_data

    def post(self):
        data = request.get_json(force=True)
        
        # Validate head_id exists
        if not Doctor.query.get(data['head_id']):
            return {'message': 'Doctor not found'}, 400
        
        new_dept = Department(
            department_id=data['department_id'],
            name=data['name'],
            head_id=data['head_id']
        )
        db.session.add(new_dept)
        db.session.commit()
        
        return {
            'department_id': new_dept.department_id,
            'name': new_dept.name,
            'head_id': new_dept.head_id
        }, 201

class DepartmentResource(Resource):
    """APIs for single department"""
    
    def get(self, department_id):
        dept = Department.query.get_or_404(department_id)
        return {
            'department_id': dept.department_id,
            'name': dept.name,
            'head_id': dept.head_id,
            'doc_first_name': dept.head.doc_first_name,
            'doc_last_name': dept.head.doc_last_name
        }

    def put(self, department_id):
        dept = Department.query.get_or_404(department_id)
        data = request.get_json(force=True)
        
        # Validate head_id exists
        if not Doctor.query.get(data['head_id']):
            return {'message': 'Doctor not found'}, 400
        
        dept.name = data['name']
        dept.head_id = data['head_id']
        db.session.commit()
        
        return {
            'department_id': dept.department_id,
            'name': dept.name,
            'head_id': dept.head_id
        }

    # Add delete method if needed
    def delete(self, department_id):
        dept = Department.query.get_or_404(department_id)
        db.session.delete(dept)
        db.session.commit()
        return {'message': 'Department deleted'}, 204