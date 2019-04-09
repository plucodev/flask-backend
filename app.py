import os
import sqlalchemy
from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Item
  
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
  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))