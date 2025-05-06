from flask import request, jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")
db = client.TestDB
testingDB = db["Tests"]

class MongoDB:
    def __init__(self):
        self.db = MongoClient("mongodb://db:27017").BackEnd
    def getClient(self):
        return self.db
# class createTest(Resource):
#     def post(self):
#         testingDB.insert_one({
#             "Hello":1,
#             "Bye":"Test"
#         })
#         retJSon = {
#             "status": 201,
#             "msg": "Post in another file created"
#         }
#         return jsonify(retJSon)
#     def get(self):
#         retJson = {
#             "status": 200,
#             "msg": testingDB.find({"Hello":1})[0]["Bye"]
#         }
#         return jsonify(retJson)
