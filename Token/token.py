import jwt
from flask import request, jsonify
import datetime

secretKey = "fakfha(*&&KJSH23"


def token_required(f):
    def decoration(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'You must login'}), 403
        try:
            personId=jwt.decode(token.split(' ')[1], secretKey, algorithms="HS256")["Info"]["id"]
        except Exception as error:
            return jsonify({"error": "Invalid Token"}), 401

        return f(id=personId, *args, **kwargs)

    return decoration


def admin_token(f):
    def decoration(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'You must login'}), 403
        try:
            if jwt.decode(token.split(' ')[1], secretKey, algorithms="HS256")['Info']["Type"].lower() != 'admin':
                return jsonify({"error": "Not An Admin"}), 401

        except Exception as error:
            return jsonify({"error": "Invalid Token"})
        return f(*args, **kwargs)

    return decoration


def encode(userType,id, exp=datetime.datetime.utcnow() + datetime.timedelta(minutes=10)):
    return jwt.encode({"Info": {"Type":userType,"id":id}, "exp": exp}, secretKey)
