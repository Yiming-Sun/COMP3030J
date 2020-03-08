from blogapp import db
from wtforms.ext.sqlalchemy.fields import QuerySelectField



class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    emid = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)
    animal = db.Column(db.String(120), index=True)
    workplace = db.Column(db.String(120), index=True)

class Id(db.Model):
    cid = db.Column(db.String(120), unique=True, primary_key=True)






class NewAppointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant = db.Column(db.String(20), index=True, nullable=False)
    date = db.Column(db.DateTime, index=True, nullable=False)
    petType = db.Column(db.Integer, index=True, nullable=False)
    doctor = db.Column(db.Integer, index=True, nullable=False)

    phoneNo = db.Column(db.String(20), index=True, nullable=False)
    comment = db.Column(db.String, default="")
    user_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    cus_appoint = db.relationship('Customer', backref=db.backref('Customer'))

    def __repr__(self):
        return '<User {}>'.format(self.username)
