from blogapp import db




class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)


class NewAppointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant = db.Column(db.String(20), index=True, nullable=False)
    date = db.Column(db.String, index=True, nullable=False)
    petType = db.Column(db.Integer, index=True, nullable=False)
    petName = db.Column(db.String(20), index=True, nullable=False)
    doctor = db.Column(db.Integer, index=True, nullable=False)
    phoneNo = db.Column(db.String(20), index=True, nullable=False)
    comment = db.Column(db.String, default="")
    condition = db.Column(db.Integer, index=True, default=1, nullable=False)
    op_date = db.Column(db.String, index=True)
    op_time = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    cus_appoint = db.relationship('Customer', backref=db.backref('Customer'))

    def to_json(self):
        return{
            "id" : self.id,
            "applicant" : self.applicant,
            "date" : self.date,
            "petType" : self.petType,
            "doctor" : self.doctor,
            "phoneNo" : self.phoneNo,
            "comment" : self.comment,
            "user_id" : self.user_id,
        }
