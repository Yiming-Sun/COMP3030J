from blogapp import app, db
from flask import Flask, render_template, request, flash, redirect, url_for, session
from blogapp.forms import AppointmentForm
from blogapp.models import NewAppointment
from blogapp.config import Config
import os

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home')


@app.route('/New_appointment')
def New_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        name = form.applicant.data
    return render_template('New_appointment.html', title='Home',form=form)


@app.route('/My_appointment')
def My_appointment():
    return render_template('My_appointment.html', title='Home')


@app.route('/sign_in')
def sign_in():
	return render_template('sign_in.html', title='Home')

@app.route('/sign_up')
def sign_up():
	return render_template('sign_up.html', title='Home')
