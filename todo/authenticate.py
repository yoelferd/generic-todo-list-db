from flask import request, jsonify
import functools
import sqlite3
import base64
import hashlib
import uuid

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users (users varchar, password varchar)")

users = {"Booker": "password",
         "Annabel": "password",
         "Steve": "password",
         "Tawny": "password",
         "Kasha": "password",
         "Tameika": "password",
         "Marie": "password",
         "Samual": "password",
         "Cyrus": "password",
         "Joya": "password"}

#for val in users:
    #c.execute(f"INSERT INTO users values({val}, {users[val]})")

def hashsalt(password):
    salt = uuid.uuid4().hex
    return hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

hashed = [(val, hashsalt(users[val])) for val in users]
print(hashed)

def ok_user_and_password(username, password):
    """Test whether the supplied username and password match."""
    salt = uuid.uuid4().hex
    return users.get(username) == hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

print(ok_user_and_password("Booker",hashsalt("password")))

def authenticate():
    """ Return a response indicating a failure to authenticate."""
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Main"'

    return resp


def requires_authorization(f):
    """A python decorator which requires HTTP basic authentication."""

    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not ok_user_and_password(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
