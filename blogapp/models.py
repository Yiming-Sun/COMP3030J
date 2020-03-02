from blogapp import db


class NewAppointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant = db.Column(db.String(20), index=True, nullable=False)
    date = db.Column(db.DateTime, index=True, nullable=False)
    petType = db.Column(db.String(20), index=True, nullable=False)
    doctor = db.Column(db.String(20), index=True, nullable=False)
    phoneNo = db.Column(db.String(20), index=True, nullable=False)
    comment = db.Column(db.String, default="")

    def __repr__(self):
        return '<User {}>'.format(self.username)

