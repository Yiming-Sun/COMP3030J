from flask_wtf import FlaskForm, RecaptchaField
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

from flask_babel import Babel, gettext as _
from blogapp import app
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)



def possible_doc():
    return Employee.query


def poss_name():
    return [r.username for r in db.session.query(Employee).all()]


# Yiming Sun(2020/3/30)
class C_personal_space(FlaskForm):
    picture = FileField(_('choose picture'))
    username = StringField(_('Username'), validators=[DataRequired()])
    email = StringField(_('E-mail'), validators=[DataRequired()])
    phone = StringField(_('Phone Number'), validators=[DataRequired()])
    nickname = StringField(_('Nickname'))
    gender = SelectField(_('Gender'), coerce=int, choices=[(1, 'male'), (2, 'female')])
    nationality = StringField(_('Nationality'))
    city = StringField(_('City'))
    address = StringField(_('Address'))
    personal_signature = StringField(_('Personal signature'))
    submit = SubmitField(_("Save"))


# Yiming Sun(2020/3/30)
class E_personal_space(FlaskForm):
    picture = FileField(_('choose picture'), default=None)
    username = StringField(_('Username'), validators=[DataRequired()])
    email = StringField(_('E-mail'), validators=[DataRequired()])
    phone = StringField(_('Phone Number'), validators=[DataRequired()])
    nickname = StringField(_('Nickname'))
    gender = SelectField(_('Gender'), coerce=int, choices=[(1, _('male')), (2, _('female'))])
    animal = StringField(_('Animal type'), validators=[DataRequired()])
    workplace = StringField(_('Workplace'), validators=[DataRequired()])
    nationality = StringField(_('Nationality'))
    city = StringField(_('City'))
    address = StringField(_('Address'))
    personal_signature = StringField(_('Personal signature'))
    submit = SubmitField(_("Save"))


# Yiming Sun(2020/3/14)
class AppointmentForm(FlaskForm):
    applicant = StringField(_('Applicant'), validators=[DataRequired()])
    phoneNo = StringField(_('Phone Number'), validators=[DataRequired()])
    date = DateField(_('Date(tip: you can just select the next ten days)'), format='%Y-%m-%d', validators=[DataRequired()])
    appointment_time = SelectField(_('Appointment Time'), coerce=int,
                                   choices=[(1, _('--choose time--')),(2, '8:00 - 10:00'), (3, '10:00 - 12:00'), (4, '13:00 - 15:00'),
                                            (5, '15:00 - 17:00')])
    petType = SelectField(_('Pet Type'), coerce=int, choices=[(1, _('dog')), (2, _('cat'))])
    petName = StringField(_('Pet Name'), validators=[DataRequired()])
    doctor = SelectField(_('Select Doctor'), coerce=int, choices=[(1, _('Allen')), (2, _('Fred'))])
    # doctor = QuerySelectField(label='Select Doctor', validators=[validators.required()], query_factory=poss_name,
    #                           allow_blank=True)
    comment = StringField(_('Symptom'))
    submit = SubmitField(_('Submit'))

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in Employee.query.all()]

    def select_doctor(self, place):
        # super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in
                               Employee.query.filter(and_(Employee.animal == "Dog", Employee.workplace == place)).all()]


# Yiming Sun(2020/3/14)
class UrgentAppointment(FlaskForm):
    applicant = StringField(_('Applicant'), validators=[DataRequired()])
    phoneNo = StringField(_('Phone Number'), validators=[DataRequired()])
    date = DateField(_('Date(tip: you can just select the next ten days, including today)'), format='%Y-%m-%d',
                     validators=[DataRequired()])
    appointment_time = SelectField(_('Appointment Time'), coerce=int,
                                   choices=[(1, _('--choose time--')),(2, '8:00 - 10:00'), (3, '10:00 - 12:00'), (4, '13:00 - 15:00'),
                                            (5, '15:00 - 17:00')])
    petType = SelectField(_('Pet Type'), coerce=int, choices=[(1, _('dog')), (2, _('cat'))])
    petName = StringField(_('Pet Name'), validators=[DataRequired()])
    doctor = SelectField(_('Select Doctor'), coerce=int, choices=[(1, 'Allen'), (2, 'Fred')], )
    operationDate = DateField(_('Date'), format='%Y-%m-%d', validators=[DataRequired()])
    operationTime = SelectField(_('Time'), coerce=int,
                                choices=[(1, _('--choose time--')),(2, '8:00 - 10:00'), (3, '10:00 - 12:00'), (4, '13:00 - 15:00'),
                                            (5, '15:00 - 17:00')])
    comment = StringField(_('Symptom'))
    submit = SubmitField(_('Submit'))

    def __init__(self, *args, **kwargs):
        super(UrgentAppointment, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in Employee.query.all()]

    def select_doctor(self, place):
        # super(AppointmentForm, self).__init__(*args, **kwargs)
        self.doctor.choices = [(v.id, v.username) for v in
                               Employee.query.filter(and_(Employee.animal == "Dog", Employee.workplace == place)).all()]


class LoginForm(FlaskForm):
    username = StringField(_('Username'), validators=[DataRequired()])
    password = PasswordField(_('Password'), validators=[DataRequired()])
    submit = SubmitField(_('Sign In'))


class SignForm_C(FlaskForm):
    username = StringField(_('Username'), validators=[DataRequired()])
    password = PasswordField(_('Password'), validators=[DataRequired()])
    repeat_password = PasswordField(_('Repeat Password'), validators=[DataRequired(), EqualTo('password',
                                                                                           message=_("two passwords are not equal"))])
    nickname = StringField(_('Nickname'), validators=[DataRequired()])
    email = StringField(_('Email'), validators=[DataRequired(), Email()])
    phone = StringField(_("Phone"), validators=[DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField(_('Sign Up'))


class SignForm_E(FlaskForm):
    username = StringField(_('Username'), validators=[DataRequired()])
    id = StringField(_('Employee ID'), validators=[DataRequired()])
    password = PasswordField(_('Password'), validators=[DataRequired()])
    repeat_password = PasswordField(_('Repeat Password'), validators=[DataRequired(), EqualTo('password', message=_("not "
                                                                                                               "equal"))])
    nickname = StringField(_('Nickname'), validators=[DataRequired()])
    email = StringField(_('Email'), validators=[DataRequired(), Email()])
    phone = StringField(_("Phone"), validators=[DataRequired()])
    animal = SelectField(_('Animal'), coerce=int, choices=[(1, _('Dog')), (2, _('Cat'))])
    workplace = SelectField(_('Workplace'), coerce=int, choices=[(1, _('Beijing')), (2, _('Shnaghai')), (3, _('Chengdu'))])
    #recaptcha = RecaptchaField()
    submit = SubmitField(_('Sign Up'))



class modify_password(FlaskForm):
    pre_password = StringField('previous password', validators=[DataRequired()])
    new_password = StringField('new password', validators=[DataRequired()])
    comfirm_password = StringField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Modify Password')


class ResetPasswordRequestForm(FlaskForm):
    """重置密码请求表单"""
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    submit = SubmitField('请求密码重置')

class ResetPasswordForm(FlaskForm):
    """重置密码表单"""
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('请求密码重置')
