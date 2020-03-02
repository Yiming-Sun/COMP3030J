from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AppointmentForm(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    date = DateField('Date',format='%Y-%m-%d', validators=[DataRequired()])
    petType = SelectField('Pet Type', choices=[(1, 'dog'), (2, 'cat')])
    doctor = SelectField('Select Doctor', choices=[(1, 'a1'), (2, 'a2')])
    phoneNo = StringField('Phone Number', validators=[DataRequired()])
    comment = StringField('Comment')
    submit = SubmitField('Submit')
