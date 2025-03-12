from flask import Flask, request, jsonify
from models import User, Category, Expense, Budget, session

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": Welcome to the Expense Tracker API!})

@app.route('/users', methods=['GET'])
def get_users():
    users = session.query(User).all()   #fetch all users from database
    
    user_list = []
    for user in users:
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }

        user_list.append(user_data)

    return jsonify(user_list)

