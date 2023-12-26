from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))


class Reward(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    reward_name = db.Column(db.String(30))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),unique=True)
    user = db.relationship('User',backref='rewards')

class UserSchema(ma.ModelSchema):
    class Meta:
        model=User

app.route('/')        
def index():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(users)
    return jsonify({'user':output})



if __name__ == '__main__':
    app.run(debug=True)