import os
import sqlalchemy
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from models import db, Item, User
  
app = Flask(__name__)
##Setting the place for the db to run
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/contacts-flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initializing the db (after registering the Models)
db.init_app(app)
#migration engine
migrate = Migrate(app, db)
  
@app.route('/')
def hello():
    return jsonify({ "hello": "World" })
    
@app.route('/users')
def user_list():
    users = User.query.all()
    response = []
    for u in users:
        user = u.to_OrderedDict()
        response.append(user)
    
    return jsonify({"Users": response})

@app.route('/user/add', methods=['POST'])
def adduser():
    user_info = request.get_json() or {}
    item = User(name=user_info["name"],
            last_name=user_info["last_name"],
            email=user_info["email"],
            is_logged_in=user_info["is_logged_in"]              
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({"response": item.to_OrderedDict()})
    # return jsonify({"response": "User " + item.name + " added" })

@app.route('/user/<user_id>', methods=['DELETE'])
def deleteuser(user_id):
     if user_id is not None:
        currentUser = User.query.get(user_id)
        db.session.delete(currentUser)
        db.session.commit()
        return jsonify( {"deleted": "The user " + currentUser.name + " has been deleted succesfully!"} )

#   ******************************
#   METHOD TO UPDATE A SINGLE USER
#   ******************************
#
# @app.route('/user/<user_id>', methods=['PUT'])
# def updateuser(user_id):
#     if user_id is not None:
#         currentUser = User.query.get(user_id)
#         updatedUser = request.get_json() or {}
#         item = currentUser(name=updatedUser["name"],
#             last_name=updatedUser["last_name"],
#             email=updatedUser["email"],
#             is_logged_in=updatedUser["is_logged_in"]

#     )
#     db.session.add(item)
#     db.session.commit()
#     return jsonify({"ok"})

@app.route('/user/<user_id>', methods=['GET'])
def singleuser(user_id):
    if user_id is not None:
        currentUser = User.query.get(user_id)
        return jsonify( {"response": currentUser.to_OrderedDict()} )
  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))