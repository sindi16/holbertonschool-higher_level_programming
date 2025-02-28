#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store users
users = {}


@app.route("/")
def home():
    """Home route returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the API status."""
    return jsonify({"status": "OK"})


@app.route("/users/<username>")
def get_user(username):
    """Fetches a user by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user via POST request."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    user_data = request.get_json()
    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
