## Final-Project
CS:3980:0001 Final Project
Cade, Guadalupe, Noah

# GroceryGo

![GroceryGo](https://github.com/Khayde88/Final-Project/assets/144306042/31a34f8e-beb0-4713-a9a3-5e773fa55ba1)

### Login
![Login](https://github.com/Khayde88/Final-Project/assets/144306042/9d7fbacd-130e-4e53-8ad0-53e1ed9f58db)

### Registration
![Register](https://github.com/Khayde88/Final-Project/assets/144306042/c5b8eb40-747e-45da-ab7e-8e80cdbd465e)

### Create Grocery List
![CreateList](https://github.com/Khayde88/Final-Project/assets/144306042/f72a72c5-eaa9-4734-9146-1b34a94fbd13)

### Edit List
![EditList](https://github.com/Khayde88/Final-Project/assets/144306042/43826ad2-3ce6-4a0c-b4b2-c507160f3abb)

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
