# FastAPI + MongoDB CRUD API

This is a simple CRUD API built using FastAPI and MongoDB (via PyMongo).

## Features

- Create, Read, Update, Delete (CRUD) operations
- MongoDB integration using PyMongo
- Environment-based MongoDB connection
- Data validation using Pydantic models
- JSON serialization for ObjectId

## Setup Instructions

1. Clone the repository:

git clone https://github.com/Ajaygohil25/fastapi-mongoDB.git
cd fastapi-mongoDB

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt
Create a .env file and add:

4. Create a .env file and add:
DB_USER_NAME=your_username
DB_PASSWORD=your_password

5. Run the app:
uvicorn main:app --reload
Visit: http://localhost:8000/docs

API Endpoints

| Method | Endpoint  | Description        |
| ------ | --------- | ------------------ |
| POST   | /add-post | Create a TODO item |
| GET    | /         | Get all TODOs      |
| PUT    | /{id}     | Update a TODO      |
| DELETE | /{id}     | Delete a TODO      |

