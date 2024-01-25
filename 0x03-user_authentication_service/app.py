#!/usr/bin/env python3

from flask import Flask, jsonify, request, abort
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


@app.route("/sessions", methods=["POST"])
def session_user():
    """POST route for user session"""
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password) is True:
        session_id = AUTH.create_session(email)
        response = jsonify({'email': email, 'message': 'logged in'})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route("/logout", methods=["DELETE"])
def delete_user():
    """DELETE route for user session"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user_id)
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
    """route to find the user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    message = {"email": user.email}
    return jsonify(message), 200


@app.route("/reset_password", methods=["POST"])
def reset_password():
    """route to reset password of user"""
    email = request.form['email']
    reset_token = AUTH.get_reset_password_token(email)
    if reset_token is None:
        abort(403)
    message = {"email": email, "reset_token": reset_token}
    return jsonify(message), 200


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """route to update password of user"""
    try;
        email = request.form['email']
        reset_token = request.form['reset_token']
        new_password = request.form['new_password']
        AUTH.update_password(reset_token, new_password)
        message = {"email": email, "message": "Password updated"}
        return jsonify(message), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
