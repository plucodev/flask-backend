from flask_sqlalchemy import SQLAlchemy
  
db = SQLAlchemy()
  
#Example model Item 
#It represents an Item in a list
#you can use any name, first letter in CAPS
  
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return 'Item: %s (%s)' % (self.text, self.created_on)
        
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    is_logged_in = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return 'User: %s, %s' % (self.name, self.last_name)
    
    def to_OrderedDict(self):
        return { 
          "id": self.id, 
          "name": self.name, 
          "last_name": self.last_name, 
          "email": self.email ,
          "is_logged_in": self.is_logged_in
        }
    