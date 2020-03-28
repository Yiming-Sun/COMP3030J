from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired


from blogapp import app, db
from flask import Flask, jsonify, render_template, request, flash, redirect, url_for, session
from blogapp.models import Employee, NewAppointment, Customer, Id, ConfigurationC, ConfigurationE, AnswerQuestion, \
    Question

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


class ConfigurationFormC(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    Phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class ConfigurationFormE(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    Phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Confirm')