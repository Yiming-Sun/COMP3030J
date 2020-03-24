from blogapp import app, db
from flask import Flask, jsonify, render_template, request, flash, redirect, url_for, session
from blogapp.forms import AppointmentForm, LoginForm, UrgentAppointment
from blogapp.models import Employee,NewAppointment, Customer,Id, AlchemyJsonEncoder

from werkzeug.security import generate_password_hash, check_password_hash
from blogapp.config import Config
import os
import json


petT = {
    "1": "Dog",
    "2": "Cat"
}

condition_dict = {
    1:"appoint success",
    2:"diagnosing",
    3:"reserve operation",
    4:"operating",
    5:"finish operation",
    6:"pay for medicine",
    7:"out"
}

doctorN = {
    "1": "Allen",
    "2": "Fred"
}


#自定义过滤器
@app.template_filter('getCondition')
def hash(h,key):

    if key in h.keys():
        return h[key]
    else:
        return None



@app.route('/')
@app.route('/index')
def index():
    # session['USERNAME'] = 1
    return render_template('index.html', title='Home')

#Yiming Sun(2020/3/14)
@app.route('/appointment_modify/<int:id>', methods=['GET','POST'])
def appointment_modify(id):
    form = AppointmentForm()
    if not session.get("USERNAME") is None:

        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()

        if form.validate_on_submit():
            appointment.date = form.date.data
            appointment.petType = form.petType.data
            appointment.petName = form.petName.data
            appointment.doctor = form.doctor.data
            appointment.comment = form.comment.data
            db.session.commit()
            return redirect(url_for('My_appointment'))
        else:

            form.applicant.data = appointment.applicant
            #form.date.data = appointment.date
            form.petType.data = appointment.petType
            form.petName.data = appointment.petName
            form.doctor.data = appointment.doctor
            form.phoneNo.data = appointment.phoneNo
            form.comment.data = appointment.comment

        return render_template('appointment_modify.html',form=form)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('sign_in'))


@app.route('/appointment_urgent_modify/<int:id>', methods=['GET','POST'])
def appointment_urgent_modify(id):
    form = UrgentAppointment()
    if not session.get("USERNAME") is None:

        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()

        if form.validate_on_submit():
            appointment.date = form.date.data
            appointment.petType = form.petType.data
            appointment.petName = form.petName.data
            appointment.doctor = form.doctor.data
            appointment.op_date = form.operationDate.data
            appointment.op_time = form.operationTime.data
            appointment.comment = form.comment.data
            db.session.commit()
            return redirect(url_for('My_appointment'))
        else:

            form.applicant.data = appointment.applicant
            #form.date.data = appointment.date
            form.petType.data = appointment.petType
            form.petName.data = appointment.petName
            form.doctor.data = appointment.doctor
            form.operationTime.data = appointment.op_time
            form.phoneNo.data = appointment.phoneNo
            form.comment.data = appointment.comment

        return render_template('appointment_urgent_modify.html',form=form)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('sign_in'))


#Yiming Sun(2020/3/14)
@app.route('/appointment_trace/<int:id><int:condition>',methods=['GET','POST'])
def appointment_trace(id,condition):

    app = NewAppointment.query.filter(NewAppointment.id == id).first()

    if request.method == 'GET' and request.values.get("type") == "hasArrival":
        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
        appointment.condition = 2 #诊断中
        db.session.commit()
    elif request.method == 'GET' and request.values.get("type") == "finishDiagnose":
        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
        appointment.condition = 3 #预约手术
        db.session.commit()
    elif request.method == 'GET' and request.values.get("type") == "finishOperation":
        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
        appointment.condition = 5 #手术结束
        db.session.commit()


    return render_template('appointment_trace.html',condition=condition,id=id,user_type=session['USERTYPE'],app=app)


#Yiming Sun(2020/3/14)
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
            appointment = NewAppointment(app_type=1,applicant=name,petName=petName,user_id=user_id,date=date,petType=petType,doctor=doctor,phoneNo=phoneNo,comment=comment)
            db.session.add(appointment)
            db.session.commit()
            flash('done')
            return redirect(url_for('My_appointment'))

        elif request.method == "POST":

            type = request.values.get("type")
            print(petT[type])
            doctors = Employee.query.filter(petT[type] == Employee.animal).all()
            name_list = []
            for doctor in doctors:
                name_list.append(doctor.username)
            print(name_list)
            return json.dumps(name_list, ensure_ascii=False)

    return render_template('New_appointment.html', title='Home',form=form)

#Yiming Sun(2020/3/14)
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
            appointment = NewAppointment(app_type=2,op_time=op_time, op_date=op_date, applicant=name,petName=petName,user_id=user_id,date=date,petType=petType,doctor=doctor,phoneNo=phoneNo,comment=comment)
            db.session.add(appointment)
            db.session.commit()
            flash('done')
            return redirect(url_for('My_appointment'))

        elif request.method == "POST":

            type = request.values.get("type")
            print(petT[type])
            doctors = Employee.query.filter(petT[type] == Employee.animal).all()
            name_list = []
            for doctor in doctors:
                name_list.append(doctor.username)
            print(name_list)
            return json.dumps(name_list, ensure_ascii=False)

    return render_template('Urgent_appointment.html', title='Home',form=form)

#Yiming Sun(2020/3/14)
@app.route('/My_appointment',methods=['GET','POST'])
def My_appointment():

    if not session.get("USERNAME") is None:

        if request.method == 'POST':

            if request.values.get("type") == "delete":
                d = dict()
                index = request.values.get("appointment_id")
                item = NewAppointment.query.filter(NewAppointment.id == index).first()
                db.session.delete(item)
                db.session.commit()
            #appointments = NewAppointment.query.filter(NewAppointment.user_id == session.get("USERNAME")).all()
            #data = NewAppointment.to_json(appointments)
            #print(data)
                return "delete success"

            elif request.values.get("type") == "query":
                petName = request.values.get("pet_name")
                if len(petName) == 0:
                    items = NewAppointment.query.filter(NewAppointment.user_id == session.get("USERNAME")).all()
                    print("1111111111111111")
                    print(items)
                else:
                    items = NewAppointment.query.filter(NewAppointment.petName == petName).all()
                data = NewAppointment.to_json(items)
                print(data)
                return json.dumps(data, ensure_ascii=False)

        else:
            my_appointments = NewAppointment.query.filter(NewAppointment.user_id == session.get("USERNAME")).all()

            return render_template('My_appointment.html', title='Home',my_appointments=my_appointments,petT=petT, condition_dict=condition_dict)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('sign_in'))




@app.route('/Doc_appointment', methods=['GET', 'POST'])
def Doc_appointment():
    if not session.get("USERNAME") is None:

        if request.method == "POST":
            id = request.values.get("appointment_id")
            print(id)
            appointment = NewAppointment.query.filter(NewAppointment.id==id).first()
            if appointment.app_type == 1:
                appointment.app_type = 2
            else:
                appointment.app_type = 1
            db.session.commit()
            return "success"
        else:

            my_e = Employee.query.filter(Employee.username == session.get("USERNAME")).first()
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
            session["USERTYPE"] = "customer"
            return redirect(url_for('appointment_type'))
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
            session["USERTYPE"] = "employee"
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
