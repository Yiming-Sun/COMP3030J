from blogapp import app, db
from flask import Flask, jsonify, render_template, request, flash, redirect, url_for, session
from blogapp.forms import AppointmentForm, LoginForm
from blogapp.models import Employee,NewAppointment, Customer,Id

from werkzeug.security import generate_password_hash, check_password_hash
from blogapp.config import Config
import os


@app.route('/')
@app.route('/index')
def index():
    # session['USERNAME'] = 1
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
            phoneNo = form.phoneNo.data
            comment = form.comment.data
            user_id = session.get("USERNAME")
            appointment = NewAppointment(applicant=name, user_id=user_id, date=date, petType=petType, doctor=doctor,
                                         phoneNo=phoneNo, comment=comment)
            db.session.add(appointment)
            db.session.commit()
            flash('done')
            return redirect(url_for('My_appointment'))

    return render_template('New_appointment.html', title='Home', form=form)


@app.route('/My_appointment')
def My_appointment():
    if not session.get("USERNAME") is None:
        print(session.get("USERNAME"))
        my_appointments = NewAppointment.query.filter(NewAppointment.user_id == session.get("USERNAME")).all()
        return render_template('My_appointment.html', title='Home', my_appointments=my_appointments)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('login'))

@app.route('/Doc_appointment', methods=['GET', 'POST'])
def Doc_appointment():
    if not session.get("USERNAME") is None:
        print(session.get("USERNAME"))
        my_e = Employee.query.filter(Employee.username == session.get("USERNAME")).first()
        print(my_e)
        my_appointments = NewAppointment.query.filter(NewAppointment.doctor == my_e.id).all()
        return render_template('Appointment_doc.html', title='Home', my_appointments=my_appointments)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('login'))


# @app.route('/sign_in', methods=['GET', 'POST'])
# def sign_in():
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['USERNAME'] = Customer.query.first().id
#         return redirect(url_for('New_appointment'))
#     return render_template('sign_in.html', title='Home',form=form)

@app.route('/login_c', methods=['GET', 'POST'])
def sign_in_c():
    form = LoginForm()
    if form.validate_on_submit():
        user_in_db = Customer.query.filter(Customer.username == form.username.data).first()
        if not user_in_db:
            flash("No user found with username: {}")
            flash('No user found with username: {}'.format(form.username.data))
            return redirect(url_for('sign_in'))
        if (check_password_hash(user_in_db.password_hash, form.password.data)):
            flash('Login success!')
            session["USERNAME"] = user_in_db.username
            return redirect(url_for('My_appointment'))
        flash('Incorrect Password')
        return redirect(url_for('index'))
    return render_template('sign_in.html', title='Sign In', form=form)

@app.route('/login_d', methods=['GET', 'POST'])
def sign_in_d():
    form = LoginForm()
    if form.validate_on_submit():
        doc_in_db = Employee.query.filter(Employee.username == form.username.data).first()
        if not doc_in_db:
            flash("No user found with username: {}")
            flash('No user found with username: {}'.format(form.username.data))
            return redirect(url_for('sign_in'))
        if (check_password_hash(doc_in_db.password_hash, form.password.data)):
            flash('Login success!')
            session["USERNAME"] = doc_in_db.username
            print('sdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            return redirect(url_for('Doc_appointment'))
        flash('Incorrect Password')
        return redirect(url_for('index'))
    return render_template('sign_in.html', title='Sign In', form=form)

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html', title='Home')


@app.route('/appointment_type')
def appointment_type():
    return render_template('appointment_type.html', title="home")


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
                user = Customer(username=username, email=email, password_hash=passw_hash, phone=phone)
                db.session.add(user)
                db.session.commit()
                session['USERNAME'] = username
                print(session['USERNAME'])
                return redirect(url_for('appointment_type'))
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
                    user = Employee(username=username, password_hash=passw_hash, email=email, emid=emplid, phone=phone,
                                    animal=animal,
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


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # 获取用户上传的文件对象
        f = request.files['faceImg']
        # 获取上传文件的文件名
        # print(f.filename)
        # 获取当前项目的目录位置;
        basepath = os.path.dirname(__file__)
        # print(__file__)       # /root/PycharmProjects/day34/app.py
        # print(basepath)       # /root/PycharmProjects/day34
        # /root/PycharmProjects/day34/static/img/face/xxx.png
        # 拼接路径， 保存到本地的位置;
        filepath = os.path.join(basepath, 'static', 'img', 'face', f.filename)

        # 保存文件
        f.save(filepath)
        flash("上传文件%s成功" % (f.filename))
        return redirect(url_for('upload'))
    else:
        return render_template('upload.html')


def tsest():
    print("right")
