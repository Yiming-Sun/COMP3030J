from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, PasswordField, BooleanField, SubmitField, validators, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from sqlalchemy import and_
from blogapp import db
from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask import Flask, jsonify, render_template, request, flash, redirect, url_for, session
from blogapp.models import Employee, NewAppointment, Customer, Id, AnswerQuestion, \
    Question

from wtforms import form, fields, validators, widgets
from wtforms.ext.sqlalchemy.fields import QuerySelectField


def possible_doc():
    return Employee.query


def poss_name():
    return [r.username for r in db.session.query(Employee).all()]


# Yiming Sun(2020/3/30)
class C_personal_space(FlaskForm):
    picture = FileField('picture')
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    nickname = StringField('Nickname')
    gender = SelectField('Gender', coerce=int, choices=[(1, 'male'), (2, 'female')])
    nationality = StringField('Nationality')
    city = StringField('City')
    address = StringField('Address')
    personal_signature = StringField('Personal signature')
    submit = SubmitField("Save")


# Yiming Sun(2020/3/30)
class E_personal_space(FlaskForm):
    picture = FileField('picture', default=None)
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    nickname = StringField('Nickname')
    gender = SelectField('Gender', coerce=int, choices=[(1, 'male'), (2, 'female')])
    animal = StringField('Animal type', validators=[DataRequired()])
    workplace = StringField('Workplace', validators=[DataRequired()])
    nationality = StringField('Nationality')
    city = StringField('City')
    address = StringField('Address')
    personal_signature = StringField('Personal signature')
    submit = SubmitField("Save")


# Yiming Sun(2020/3/14)
class AppointmentForm(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    phoneNo = StringField('Phone Number', validators=[DataRequired()])
    date = DateField('Date(tip: you can just select the next ten days)', format='%Y-%m-%d', validators=[DataRequired()])
    appointment_time = SelectField('Appointment Time', coerce=int,
                                   choices=[(1, '8:00 - 10:00'), (2, '10:00 - 12:00'), (3, '13:00 - 15:00'),
                                            (4, '15:00 - 17:00')])
    petType = SelectField('Pet Type', coerce=int, choices=[(1, 'dog'), (2, 'cat')])
    petName = StringField('Pet Name', validators=[DataRequired()])
    doctor = SelectField('Select Doctor', coerce=int, choices=[(1, 'Allen'), (2, 'Fred')])
    # doctor = QuerySelectField(label='Select Doctor', validators=[validators.required()], query_factory=poss_name,
    #                           allow_blank=True)
    comment = StringField('Symptom')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in Employee.query.all()]

    def select_doctor(self, place):
        # super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in
                               Employee.query.filter(and_(Employee.animal == "Dog", Employee.workplace == place)).all()]


# Yiming Sun(2020/3/14)
class UrgentAppointment(FlaskForm):
    applicant = StringField('Applicant', validators=[DataRequired()])
    phoneNo = StringField('Phone Number', validators=[DataRequired()])
    date = DateField('Date(tip: you can just select the next ten days, including today)', format='%Y-%m-%d',
                     validators=[DataRequired()])
    appointment_time = SelectField('Appointment Time', coerce=int,
                                   choices=[(1, '8:00 - 10:00'), (2, '10:00 - 12:00'), (3, '13:00 - 15:00'),
                                            (4, '15:00 - 17:00')])
    petType = SelectField('Pet Type', coerce=int, choices=[(1, 'dog'), (2, 'cat')])
    petName = StringField('Pet Name', validators=[DataRequired()])
    doctor = SelectField('Select Doctor', coerce=int, choices=[(1, 'Allen'), (2, 'Fred')], )
    operationDate = DateField('Date', format='%Y-%m-%d')
    operationTime = SelectField('Time', coerce=int,
                                choices=[(1, '8:00 - 10:00'), (2, '10:00 - 12:00'), (3, '13:00 - 15:00'),
                                         (4, '15:00 - 17:00')])
    comment = StringField('Symptom')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(UrgentAppointment, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in Employee.query.all()]

    def select_doctor(self, place):
        # super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in
                               Employee.query.filter(and_(Employee.animal == "Dog", Employee.workplace == place)).all()]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class SignForm_C(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password',
                                                                                           message="two passwords are not equal")])
    nickname = StringField('Nickname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class SignForm_E(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    id = StringField('Employee ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message="not "
                                                                                                               "equal")])
    nickname = StringField('Nickname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField("Phone", validators=[DataRequired()])
    animal = SelectField('Animal', coerce=int, choices=[(1, 'Dog'), (2, 'Cat')])
    workplace = SelectField('Workplace', coerce=int, choices=[(1, 'Beijing'), (2, 'Shnaghai'), (3, 'Chengdu')])
    submit = SubmitField('Sign Up')


class modify_password(FlaskForm):
    pre_password = StringField('previous password', validators=[DataRequired()])
    new_password = StringField('new password', validators=[DataRequired()])
    comfirm_password = StringField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Modify Password')
