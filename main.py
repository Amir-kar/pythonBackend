# This is a sample Python script.
from flask import Flask, request, jsonify
from pymongo import MongoClient
from api import login

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)
client = MongoClient("mongodb://db:27017")
db = client.Sentence
users = db["User"]


# def verifyPw(username, password):
#     hashed_pw = users.find({
#         "Username": username
#     })[0]["Password"]

#     if password == hashed_pw:
#         return True
#     else:
#         return False


# def countTokens(username):
#     tokens = users.find({
#         "Username": username
#     })[0]["Tokens"]
#     return tokens

#
# api.add_resource(Register, "/reg")
# api.add_resource(Store, "/str")
# api.add_resource(Get, "/retSen")
# api.add_resource(login.Login, "/login")
# api.add_resource(login.TestToken,"/test")
app.register_blueprint(login.api)
# UserNum.insert_one({
#     'num_of_users': 0
# })
#
#
# class Visit(Resource):
#     def get(self):
#         prev_num = UserNum.find({})[0]['num_of_users']
#         new_num = prev_num + 1
#         UserNum.update_one({}, {"$set": {"num_of_users": new_num}})
#         return str("Hello User " + str(new_num))
#
#
# api.add_resource(Visit, "/visit")
#
# story = {
#     1: {
#         "name": "Hello",
#         "items": [
#             {
#                 "name": "chair",
#                 "price": 15.89
#             }
#         ]
#     },
#     2: {
#         "name": "Hello",
#         "items": [
#             {
#                 "name": "chair",
#                 "price": 15.89
#             }
#         ]
#     }
# }
#
#
# @app.get("/store")
# def getstore():
#     return {"store": story}
#
#
# i = 3
#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# @app.post("/store")
# def createPost():
#     global i
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     i += 1
#     new_store = {**store_data, "id": store_id}
#     story[store_id] = new_store
#     return new_store, 201
#
#
# @app.post("/store/<string:store_id>")
# def create_item(store_id):
#     try:
#         return story[store_id], 200
#     except KeyError:
#         return {"message": "Not Found"}, 404
#
#
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    print("done")
