import jwt

from tokens import tokenFunctions
from flask import request, jsonify, Blueprint
from db.theDBClass import MongoDB

api = Blueprint('test', __name__)



@api.route('/Hello', methods=['POST'])
@tokenFunctions.token_required
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
    retToken = tokenFunctions.encode("User",5)
    return retToken, 200

@api.route("/db1")
def testMong1():
    client = MongoDB()
    db = client.getDB()["hello"]
    db.insert_one({
            "Hello":1,
            "Bye":"Test"
        })
    return jsonify({
            "status": 200,
            "msg": db.find({"Hello":1})[0]["Bye"]
        })
    
@api.route("/db2")
def testMong2():
    client = MongoDB()
    db=client.getDB()["hello2"]
    client.closeDB()
    db.insert_one({
            "Hello":1,
            "Bye":"Test"
        })
    return jsonify({
            "status": 200,
            "msg": db.find({"Hello":1})[0]["Bye"]
        })
    

