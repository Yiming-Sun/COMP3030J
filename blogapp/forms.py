from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from sqlalchemy import and_
from blogapp import db
from blogapp.models import Employee

from wtforms import form, fields, validators, widgets
from wtforms.ext.sqlalchemy.fields import QuerySelectField


def possible_doc():
    return Employee.query


def poss_name():
    return [r.username for r in db.session.query(Employee).all()]


# Yiming Sun(2020/3/14)
class AppointmentForm(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    phoneNo = StringField('Phone Number', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    petType = SelectField('Pet Type', coerce=int, choices=[(1, 'dog'), (2, 'cat')])
    petName = StringField('Pet Name', validators=[DataRequired()])
    doctor = SelectField('Select Doctor', coerce=int)
    # doctor = QuerySelectField(label='Select Doctor', validators=[validators.required()], query_factory=poss_name,
    #                           allow_blank=True)

    comment = StringField('Symptom')
    submit = SubmitField('Submit')

    def select_doctor(self, place):
        # super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in Employee.query.filter(and_(Employee.animal == "Dog", Employee.workplace == place)).all()]



# Yiming Sun(2020/3/14)
class UrgentAppointment(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    phoneNo = StringField('Phone Number', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    petType = SelectField('Pet Type', coerce=int, choices=[(1, 'dog'), (2, 'cat')])
    petName = StringField('Pet Name', validators=[DataRequired()])
    doctor = SelectField('Select Doctor', coerce=int, choices=[(1, 'Allen'), (2, 'Fred')])
    operationDate = DateField('Date', format='%Y-%m-%d')
    operationTime = SelectField('Time', coerce=int,
                                choices=[(1, '8:00 - 10:00'), (2, '10:00 - 12:00'), (3, '13:00 - 15:00'),
                                         (4, '15:00 - 17:00')])
    comment = StringField('Symptom')
    submit = SubmitField('Submit')

    # def __init__(self, *args, **kwargs):
    #     super(UrgentAppointment, self).__init__(*args, **kwargs)
    #     self.doctor.choices = [(v.id, v.username) for v in Employee.query.filter(Employee.animal == "Dog").all()]
    def select_doctor(self, place):
        # super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in Employee.query.filter(and_(Employee.animal == "Dog", Employee.workplace == place)).all()]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
