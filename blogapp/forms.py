from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AppointmentForm(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    phoneNo = StringField('Phone Number', validators=[DataRequired()])
    date = DateField('Date', format='%Y/%m/%d', validators=[DataRequired()])
    petType = SelectField('Pet Type', coerce=int, choices=[(1, 'dog'), (2, 'cat')])
    petName = StringField('Pet Name', validators=[DataRequired()])
    doctor = SelectField('Select Doctor', coerce=int, choices=[(1, 'a1'), (2, 'a2')])
    comment = StringField('Symptom')
    submit = SubmitField('Submit')


class UrgentAppointment(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    phoneNo = StringField('Phone Number', validators=[DataRequired()])
    date = DateField('Date', format='%Y/%m/%d', validators=[DataRequired()])
    petType = SelectField('Pet Type', coerce=int, choices=[(1, 'dog'), (2, 'cat')])
    petName = StringField('Pet Name', validators=[DataRequired()])
    doctor = SelectField('Select Doctor', coerce=int, choices=[(1, 'a1'), (2, 'a2')])
    operationDate = DateField('Date', format='%Y/%m/%d')
    operationTime = SelectField('Time', coerce=int,
                              choices=[(1, '8:00 - 10:00'), (2, '10:00 - 12:00'), (3, '13:00 - 15:00'),
                                       (4, '15:00 - 17:00')])
    comment = StringField('Symptom')
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    submit = SubmitField('Log in')
