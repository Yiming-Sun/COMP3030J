from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from blogapp import db
from blogapp.models import Employee

from wtforms import form, fields, validators, widgets
from wtforms.ext.sqlalchemy.fields import QuerySelectField

def possible_doc():
    return Employee.query
def poss_name():
    return [r.username for r in db.session.query(Employee).all()]
class AppointmentForm(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    petType = SelectField('Pet Type', coerce=int, choices=[(1, 'dog'), (2, 'cat')])
    #
    doctor = SelectField('Select Doctor', coerce=int)
    # doctor = QuerySelectField(label='Select Doctor', validators=[validators.required()], query_factory=poss_name,
    #                           allow_blank=True)
    phoneNo = StringField('Phone Number', validators=[DataRequired()])
    comment = StringField('Comment')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in Employee.query.all()]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
