# # user_controller.py
# from flask import request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
# from models.user_model import User
# from database import get_users_collection

# # Route handler for user registration


# def register_user():
#     data = request.get_json()
#     username = data.get('username')
#     name = data.get('name')
#     age = data.get('age')
#     email = data.get('email')
#     mobile = data.get('mobile')
#     password = data.get('password')

#     # Check if the user already exists in the database
#     users_collection = get_users_collection()
#     existing_user = users_collection.find_one({'email': email})
#     if existing_user:
#         return jsonify({'message': 'User already exists'}), 409

#     # Create a new user instance and hash the password
#     hashed_password = generate_password_hash(password, method='sha256')
#     new_user = User(name=name, age=age, email=email, mobile=mobile,
#                     password=hashed_password, username=username)

#     # Insert the new user into the database
#     users_collection.insert_one(new_user.to_dict())

#     return jsonify({'message': 'User registered successfully'}), 201

# # Route handler for user login


# def login_user():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     # Find the user in the database based on the provided email
#     users_collection = get_users_collection()
#     user = users_collection.find_one({'email': email})

#     if user and check_password_hash(user['password'], password):
#         # Successful login
#         return jsonify({'message': 'Login successful'}), 200
#     else:
#         # Invalid credentials
#         return jsonify({'message': 'Invalid credentials'}), 401

# # Route handler for retrieving user details


# def get_user_details(user_id):
#     users_collection = get_users_collection()
#     # Exclude the password from the response
#     user = users_collection.find_one({'_id': user_id}, {'password': 0})
#     if user:
#         return jsonify(user), 200
#     else:
#         return jsonify({'message': 'User not found'}), 404


from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import User
from database import get_users_collection
import jwt
import datetime

# Route handler for user registration


def register_user():
    data = request.get_json()
    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    mobile = data.get('mobile')
    password = data.get('password')

    # Check if the user already exists in the database
    users_collection = get_users_collection()
    existing_user = users_collection.find_one({'email': email})
    if existing_user:
        return jsonify({'message': 'User already exists'}), 409

    # Create a new user instance and hash the password
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(name=name, age=age, email=email, mobile=mobile,
                    password=hashed_password, username=username)

    # Insert the new user into the database
    users_collection.insert_one(new_user.to_dict())

    return jsonify({'message': 'User registered successfully'}), 201

# Route handler for user login


def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user in the database based on the provided email
    users_collection = get_users_collection()
    user = users_collection.find_one({'email': email})

    if user and check_password_hash(user['password'], password):
        # Create a JWT token
        payload = {
            'user_id': str(user['_id']),
            # Token expiration time (1 hour)
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        secret_key = 'your_secret_key'  # Replace this with your actual secret key
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        # Successful login with token
        return jsonify({'message': 'Login successful', 'token': token}), 200
    else:
        # Invalid credentials
        return jsonify({'message': 'Invalid credentials'}), 401


def get_user_details(user_id):
    users_collection = get_users_collection()
    # Exclude the password from the response
    user = users_collection.find_one({'_id': user_id}, {'password': 0})
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found'}), 404
