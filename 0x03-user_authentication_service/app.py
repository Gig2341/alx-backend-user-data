#!/usr/bin/env python3

from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome():
    """GET route to return a JSON payload."""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=["POST"])
def register_user():
    """POST route to register user"""
    try:
        email = request.form['email']
        password = request.form['password']
        user = AUTH.register_user(email, password)
        return jsonify({'email': email, 'message': 'user created'}), 200
    except Exception:
        return jsonify({'message': 'email already registered'}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
