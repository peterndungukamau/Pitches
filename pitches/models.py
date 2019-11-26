from pitches import db
from datetime import datetime


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), unique=True, nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  image_file = db.Column(db.String(15), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  pitches = db.relationship('Pitch', backref='owner', lazy=True)

  def __repr__(self):
       return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    
class Pitch(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   category = db.Column(db.String(100), nullable=False)
   date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
   content = db.Column(db.Text, nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

   def __repr__(self):
        return f"Pitch('{self.category}', '{self.date}')"
   
