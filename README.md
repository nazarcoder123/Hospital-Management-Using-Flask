Hospital Management System Using Flask
This project is a hospital management system built with Flask. Follow the steps below to set up and run the application on your local machine.

Pre-requisites

Python 3.10.0 – Ensure you have this version installed.
PostgreSQL – Install and set up PostgreSQL for the database.
Git – To clone the repository.
Setup Instructions

1. Clone the Repository
Clone the repository to your local machine using the following command:

git clone https://github.com/nazarcoder123/Hospital-Management-Using-Flask.git

2. Create a Virtual Environment
Navigate into the project directory and create a virtual environment with Python 3.10.0:

cd Hospital-Management-Using-Flask

python3.10 -m venv .venv

Activate the virtual environment:

On Windows:
.venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
Install all required Python packages using pip:

pip install -r requirements.txt

4. Set Up the Database
Create the Database:

Open your PostgreSQL interface (e.g., psql or pgAdmin) and create a new database named hospital:

CREATE DATABASE hospital;
Initialize the Database Schema and Data:

You can either:

Option 1: Run the SQL commands from the create_tables.sql file.
Option 2: Restore the database using the provided backup (either hospital.backup or an SQL dump).
For example, to run the SQL script using psql:

psql -U your_username -d hospital -f create_tables.sql

Replace your_username with your PostgreSQL username.

5. Run the Application
Start the Flask development server:

flask run
The application should now be running on http://127.0.0.1:5000.

Additional Notes
Configuration: Make sure to adjust any configuration settings (e.g., database URI) in your Flask application if necessary.
Virtual Environment: Always activate your virtual environment before running the application to ensure all dependencies are available.
If you encounter any issues or have questions, feel free to open an issue in the repository or contact the project maintainers.

Happy coding!