## Final-Project
CS:3980:0001 Final Project
Cade, Guadalupe, Noah

# GroceryGo

## GroceryGo Backend

This project implements a backend API for the GroceryGo application using FastAPI and utilizes MongoDB for user authentication and data storage.

## Features

- User authentication using JWT (JSON Web Tokens)
- Registration of new users with roles (user or admin)
- Protected routes that require authentication
- MongoDB integration for user data storage

## Requirements

- Python 3.7+
- MongoDB
- Dependencies (install using `pip install -r requirements.txt`):
  - `fastapi`: Web framework for building APIs
  - `pymongo`: MongoDB driver for Python
  - `passlib`: Password hashing library
  - `pyjwt`: JSON Web Token implementation for Python
  - `uvicorn`: ASGI server for running FastAPI applications

## Setup

1. Clone the repository
2. Install requirements
3. Launch application

   ```bash
   git clone https://github.com/yourusername/grocerygo-backend.git

   pip install -r requirements.txt

   uvicorn main:app --reload
