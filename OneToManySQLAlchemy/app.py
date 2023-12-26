from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

db = SQLAlchemy(app)


class Company(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(100))
    employees = db.relationship('Employee',backref='company')


class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    company_id = db.Column(db.Integer,db.ForeignKey('company.id'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
   
    app.run(debug=True)