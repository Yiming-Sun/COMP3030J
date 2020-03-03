from flask import render_template, flash, redirect, url_for, session, request
from werkzeug.security import generate_password_hash, check_password_hash
from blogapp import app, db
from blogapp.forms import AppointmentForm
from blogapp.models import Costomer, Employee, Id
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
    return render_template('New_appointment.html', title='Home', form=form)


@app.route('/My_appointment')
def My_appointment():
    return render_template('My_appointment.html', title='Home')


@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html', title='Home')


@app.route('/signupC', methods=['GET', 'POST'])
def signupC():
    if request.method == "GET":
        return render_template('signupC.html')
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        phone = request.form['phone']
        if username and email and pass1 and pass2 and phone is not None:
            if pass1 == pass2:
                # print(username+" "+email+" "+pass1+" "+pass2+" "+phone+" ")
                passw_hash = generate_password_hash(pass1)
                user = Costomer(username=username, email=email, password_hash=passw_hash, phone=phone)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('index'))
            else:
                # print(username + " " + email + " " + pass1 + " " + pass2 + " " + phone + " ")
                flash('passwords are not equal')
                return redirect(url_for('signupC'))
        else:
            flash('You should fill in every line')
            return redirect(url_for('signupC'))
    return render_template('signupC.html')


@app.route('/signupE', methods=['GET', 'POST'])
def signupE():
    if request.method == "GET":
        return render_template('signupE.html')
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        phone = request.form['phone']
        animal = request.form['animal']
        workplace = request.form['workplace']
        emplid = request.form['EmployeeId']
        if username and email and pass1 and pass2 and phone is not None:
            preid = Id.query.filter(Id.cid == emplid).first()
            if preid:
                if pass1 == pass2:
                    # print(animal+" "+workplace+" "+username+" "+email+" "+pass1+" "+pass2+" "+phone+" ")
                    passw_hash = generate_password_hash(pass1)
                    user = Employee(username=username, password_hash=passw_hash, email=email, emid=emplid, phone=phone, animal=animal,
                                    workplace=workplace)
                    # i = Id(cid=emplid)
                    db.session.add(user)
                    # db.session.add(i)
                    db.session.commit()
                    return redirect(url_for('index'))
                else:
                    # print(username + " " + email + " " + pass1 + " " + pass2 + " " + phone + " ")
                    flash('passwords are not equal')
                    return redirect(url_for('signupE'))
            else:
                flash("You are not our employee, please sign up a Costomer account")
                return redirect(url_for('signupE'))
        else:
            flash('You should fill in every line')
            return redirect(url_for('signupE'))
    return render_template('signupE.html')
