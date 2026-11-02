# Student-Management-API

A Student Management REST API built using python, FastAPI and MYSQL.

This project allows users to perform CRUD (Create, Read, Update, Delete) operations on student records.

# Technologies Used

- Python
- FastAPI
- MySQL
- MySQL Connector
- Pydantic
- Uvicorn
- Python-dotenv
- Swagger UI

# Features

- Add new student records
- Retrieve all students
- Retrieve a student by ID
- Update student details
- Delete student records
- Validate request data using Pydantic
- Handle errors using appropriate HTTP status codes
- Store database credentials securely using environment variables

# API Endpoints

Method| Endpoint| Description
POST| "/students"| Add a student
GET| "/students"| Get all students
GET| "/students/{student_id}"| Get a student by ID
PUT| "/students/{student_id}"| Update student details
DELETE| "/students/{student_id}"| Delete a student

# Project Structure

Student-Management-API/
│
├── fmain.py
├── database.py
├── requirements.txt
├── .gitignore
├── README.md
└── Sqlf.sql

# Setup and Installation

1. Clone the repository

git clone https://github.com/Naseefa01/Student-Management-API/
cd Student-Management-API

2. Install dependencies

pip install -r requirements.txt

3. Configure MySQL

Create the database and students table using the provided SQL script.

4. Configure environment variables

Create a ".env" file in the project folder:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=fastapi_practice

5. Run the application

python -m uvicorn fmain:app --reload

6. Open Swagger UI

Visit:

http://localhost:8000/docs

Use Swagger UI to test the API endpoints.

# What I Learned

- Building RESTful APIs using FastAPI
- Implementing CRUD operations
- Connecting FastAPI with MySQL
- Writing SQL queries
- Validating request data using Pydantic
- Handling API errors and HTTP status codes
- Managing environment variables securely
- Testing API endpoints using Swagger UI

Created as a hands-on Python backend development project.
