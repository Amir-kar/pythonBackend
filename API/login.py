import jwt

from Token import token
from flask import request, jsonify, Blueprint

api = Blueprint('test', __name__)



@api.route('/Hello', methods=['POST'])
@token.token_required
def getSome(id=0):
    print(f"{id} requester")
    return {"talkback": "Hello There"}
# class BackendAuth:
#     def __init__(self,app):
#         self.app = app
#     @self.app
#     def login(self):
#         return "",200
#

@api.route("/getToken")
def post(id=0):
    retToken = token.encode("User",5)
    return retToken, 200
#
