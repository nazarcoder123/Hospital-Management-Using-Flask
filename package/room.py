from flask_restful import Resource, request
from sqlalchemy.exc import IntegrityError  
from package.models import db, Room

class Rooms(Resource):
    """APIs for multiple rooms"""
    
    def get(self):
        """Retrieve all rooms"""
        rooms = Room.query.all()
        return [{
            'room_no': room.room_no,
            'room_type': room.room_type,
            'available': room.available
        } for room in rooms]

    def post(self):
        """Add new room"""
        data = request.get_json(force=True)
        
        # Validate required fields
        if not all(key in data for key in ('room_no', 'room_type')):
            return {'message': 'Missing required fields (room_no, room_type)'}, 400
            
        try:
            new_room = Room(
                room_no=data['room_no'],
                room_type=data['room_type'],
                available=data.get('available', True)
            )
            db.session.add(new_room)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return {'message': 'Room number already exists'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
            
        return {
            'room_no': new_room.room_no,
            'room_type': new_room.room_type,
            'available': new_room.available
        }, 201

class RoomResource(Resource):
    """APIs for single room"""
    
    def get(self, room_no):
        """Get single room details"""
        room = Room.query.get_or_404(room_no)
        return {
            'room_no': room.room_no,
            'room_type': room.room_type,
            'available': room.available
        }

    def delete(self, room_no):
        """Delete a room"""
        room = Room.query.get_or_404(room_no)
        db.session.delete(room)
        db.session.commit()
        return {'message': 'Room deleted successfully'}, 204

    def put(self, room_no):
        """Update room details"""
        room = Room.query.get_or_404(room_no)
        data = request.get_json(force=True)
        
        if 'room_type' in data:
            room.room_type = data['room_type']
        if 'available' in data:
            room.available = data['available']
            
        db.session.commit()
        return {
            'room_no': room.room_no,
            'room_type': room.room_type,
            'available': room.available
        }