from blogapp import app, db
from flask import Flask, jsonify, render_template, request, flash, redirect, url_for, session
from blogapp.forms import AppointmentForm, LoginForm, UrgentAppointment
from blogapp.models import NewAppointment, Customer
from blogapp.config import Config
import os
import json


petT = {
    "1": "cat",
    "2": "dog"
}

doctorN = {
    "1": "Allen",
    "2": "Fred"
}


@app.route('/')
@app.route('/index')
def index():
    session['USERNAME'] = 1
    return render_template('index.html', title='Home')



@app.route('/New_appointment', methods=['GET', 'POST'])
def New_appointment():
    form = AppointmentForm()
    if not session.get("USERNAME") is None:

        if form.validate_on_submit():
            name = form.applicant.data
            date = form.date.data
            petType = form.petType.data
            doctor = form.doctor.data
            petName = form.petName.data
            phoneNo = form.phoneNo.data
            comment = form.comment.data
            user_id = session.get("USERNAME")
            appointment = NewAppointment(applicant=name,petName=petName,user_id=user_id,date=date,petType=petType,doctor=doctor,phoneNo=phoneNo,comment=comment)
            db.session.add(appointment)
            db.session.commit()
            flash('done')
            return redirect(url_for('My_appointment'))

    return render_template('New_appointment.html', title='Home',form=form)


@app.route('/My_appointment',methods=['GET','POST'])
def My_appointment():

    if not session.get("USERNAME") is None:

        if request.method == 'POST':
            d = dict()
            index = request.values.get("appointment_id")
            item = NewAppointment.query.filter(NewAppointment.id == index).first()
            db.session.delete(item)
            db.session.commit()
            appointments = NewAppointment.query.filter(NewAppointment.user_id == session.get("USERNAME")).first()
            #问题：如何把数据库中查找出来的list数据返回给ajax回调

            return jsonify(appointments.to_json())
        else:
            my_appointments = NewAppointment.query.filter(NewAppointment.user_id == session.get("USERNAME")).all()

            return render_template('My_appointment.html', title='Home',my_appointments=my_appointments,petT=petT,doctorN=doctorN)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('sign_in'))


@app.route('/Urgent_appointment', methods=['GET', 'POST'])
def Urgent_appointment():
    form = UrgentAppointment()
    if not session.get("USERNAME") is None:

        if form.validate_on_submit():
            name = form.applicant.data
            date = form.date.data
            petType = form.petType.data
            doctor = form.doctor.data
            petName = form.petName.data
            phoneNo = form.phoneNo.data
            comment = form.comment.data
            op_date = form.operationDate.data.strftime('%Y-%m-%d')
            op_time = form.operationTime.data
            user_id = session.get("USERNAME")
            appointment = NewAppointment(op_time=op_time, op_date=op_date, applicant=name,petName=petName,user_id=user_id,date=date,petType=petType,doctor=doctor,phoneNo=phoneNo,comment=comment)
            db.session.add(appointment)
            db.session.commit()
            flash('done')
            return redirect(url_for('My_appointment'))

    return render_template('Urgent_appointment.html', title='Home',form=form)

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        session['USERNAME'] = Customer.query.first().id
        return redirect(url_for('New_appointment'))
    return render_template('sign_in.html', title='Home',form=form)

@app.route('/sign_up')
def sign_up():
	return render_template('sign_up.html', title='Home')

@app.route('/appointment_type')
def appointment_type():
    return render_template('appointment_type.html', title="home")

