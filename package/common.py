import logging
from flask_restful import Resource
from package.models import db  
from sqlalchemy import text

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Common(Resource):
    """Contains common APIs for retrieving various counts for the dashboard page."""

    def get(self):
        """
        Retrieve counts for patient, doctor, appointment, medication, department, nurse,
        room, procedure, prescribes, and undergoes from the database.
        """
        # Notice the quoted "procedure" table to avoid reserved word issues
        query = text("""
            SELECT 
                (SELECT COUNT(*) FROM patient) AS patient,
                (SELECT COUNT(*) FROM doctor) AS doctor,
                (SELECT COUNT(*) FROM appointment) AS appointment,
                (SELECT COUNT(*) FROM medication) AS medication,
                (SELECT COUNT(*) FROM department) AS department,
                (SELECT COUNT(*) FROM nurse) AS nurse,
                (SELECT COUNT(*) FROM room) AS room,
                (SELECT COUNT(*) FROM "procedure") AS procedure,
                (SELECT COUNT(*) FROM prescribes) AS prescribes,
                (SELECT COUNT(*) FROM undergoes) AS undergoes
        """)
        try:
            # Execute the query using SQLAlchemy's engine.
            result = db.engine.execute(query)
            counts = dict(result.fetchone())
            logger.debug("Query executed successfully, counts: %s", counts)
        except Exception as e:
            logger.error("Error executing query: %s", e)
            return {"error": "Failed to retrieve counts"}, 500

        return counts
