from blogapp import app, db
from flask import Flask, jsonify, render_template, request, flash, redirect, url_for, session
from blogapp.forms import AppointmentForm, LoginForm, UrgentAppointment, C_personal_space, E_personal_space, SignForm_E, \
    SignForm_C, modify_password
from blogapp.models import Employee,NewAppointment, Customer,Id, AlchemyJsonEncoder, Question, AnswerQuestion

from sqlalchemy import and_, or_
from werkzeug.security import generate_password_hash, check_password_hash
from blogapp.config import Config
import os
import json
from flask import jsonify

import base64
import io
import time
import datetime
from tkinter import Image

from flask import request


petT = {
    "1": "Dog",
    "2": "Cat"
}

time_dict = {
    1:"--choose time--",
    2:"8:00 - 10:00",
    3:"10:00 - 12:00",
    4:"13:00 - 15:00",
    5:"15:00 - 17:00"
}

condition_dict = {
    1:"appoint success(1)",
    2:"diagnosing(2)",
    3:"reserve operation(3)",
    4:"operating(4)",
    5:"finish operation(5)",
    6:"pay for medicine(6)",
    7:"out(7)"
}

work_place = {
    1:"Beijing",
    2:"Shanghai",
    3:"Chengdu",
}

doctorN = {}


def get_img_path(id):
    if os.path.exists('blogapp/static/upload_photo/%s.jpg'%(id)):
            img_path = 'blogapp/static/upload_photo/%s.jpg'%(id)

    else:
        img_path = 'blogapp/static/upload_photo/default.jpg'
    figfile = io.BytesIO(open(img_path, 'rb').read())
    img = base64.b64encode(figfile.getvalue()).decode('ascii')
    return img

#自定义过滤器
@app.template_filter('getCondition')
def hash(h,key):

    if key in h.keys():
        return h[key]
    else:
        return None

#自定义医生过滤器
@app.template_filter('getDoctor')
def hash(h,key):

    if key in h.keys():
        return h[key]
    else:
        return

#自定义医生过滤器
@app.template_filter('getTime')
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

        if request.method == 'POST':
            form.applicant.data = '1'
            form.phoneNo.data = '1'
            if form.validate_on_submit():
                appointment.date = form.date.data
                appointment.petType = form.petType.data
                appointment.petName = form.petName.data
                appointment.appoint_time = form.appointment_time.data
                appointment.doctor = form.doctor.data
                appointment.comment = form.comment.data
                db.session.commit()
                return redirect(url_for('My_appointment'))
            else:
                if request.values.get("date"):

                    date = request.values.get("date")
                    appointments = NewAppointment.query.filter(NewAppointment.date == date).all()
                    appointments1 = NewAppointment.query.filter(NewAppointment.op_date == date).all()

                    result_time = {
                        1:"--choose time--",
                        2:"8:00 - 10:00",
                        3:"10:00 - 12:00",
                        4:"13:00 - 15:00",
                        5:"15:00 - 17:00"
                    }
                    #avail_time = [1,2,3,4]
                    for appointment in appointments:
                        if appointment.appoint_time in result_time.keys():
                            result_time.pop(appointment.appoint_time)

                    for appointment1 in appointments1:
                        if appointment1.op_time in result_time.keys():
                            result_time.pop(appointment.appoint_time)

                    return result_time


                if request.values.get("type"):
                    print(request.values.get("type"))
                    type = request.values.get("type")
                    #print(petT[type])
                    doctors = Employee.query.filter(and_(petT[type] == Employee.animal, session.get("PLACE") == Employee.workplace)).all()
                    name_list = {}
                    for doctor in doctors:
                        name_list[doctor.id] = doctor.username
                    #print(name_list)
                    return name_list

        else:

            form.applicant.data = appointment.applicant
            date_str = appointment.date
            form.date.data = datetime.date(*map(int,date_str.split('-')))
            form.petType.data = appointment.petType
            form.petName.data = appointment.petName
            form.doctor.data = appointment.doctor
            form.appointment_time.data = appointment.appoint_time
            form.phoneNo.data = appointment.phoneNo
            form.comment.data = appointment.comment

        return render_template('appointment_modify.html',form=form,id=id)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('index'))


@app.route('/appointment_detail/<int:id><int:type>')
def appointment_detail(id,type):
    user_type = session.get("USERTYPE")

    if not session.get("USERNAME") is None:
        print(session.get("USERNAME"))
        print(session.get("USERTYPE"))
        if type == 1:#normal
            form = AppointmentForm()
            appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
            form.applicant.data = appointment.applicant
            date_str = appointment.date
            form.date.data = datetime.date(*map(int,date_str.split('-')))
            form.petType.data = appointment.petType
            form.petName.data = appointment.petName
            form.doctor.data = appointment.doctor
            form.phoneNo.data = appointment.phoneNo
            form.comment.data = appointment.comment


        else:#urgent
            form = UrgentAppointment()
            appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
            form.applicant.data = appointment.applicant
            date_str = appointment.date
            form.date.data = datetime.date(*map(int,date_str.split('-')))
            form.petType.data = appointment.petType
            form.petName.data = appointment.petName
            form.doctor.data = appointment.doctor
            date_str = appointment.op_date
            #这个地方通过医生转换类型后会出错
            if date_str is not None:
                form.operationDate.data = datetime.date(*map(int,date_str.split('-')))
                form.operationTime.data = appointment.op_time
            #else:
                #if user_type == "customer":
                    #form.operationDate.data = "go to choose"
                    #form.operationTime.data = "go to choose"
                #else:
                    #form.operationDate.data = "user hasn't chosen yet"
                    #form.operationTime.data = "user hasn't chosen yet"
            form.phoneNo.data = appointment.phoneNo
            form.comment.data = appointment.comment


        print(form)
        return render_template('appointment_detail.html',form=form,user_type=user_type)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('index'))


@app.route('/appointment_urgent_modify/<int:id>', methods=['GET','POST'])
def appointment_urgent_modify(id):
    form = UrgentAppointment()
    if not session.get("USERNAME") is None:
        #global d
        #d = datetime.date.today()
        #d = d.replace(1900,11,11)



        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
        if request.method == 'POST':
            form.applicant.data = '1'
            form.phoneNo.data = '1'
            if appointment.condition >= 2:
                form.petName.data = appointment.petName
                form.petType.data = appointment.petType
                form.date.data = appointment.date
                form.doctor.data = appointment.doctor
                form.appointment_time.data = appointment.appoint_time
                form.comment.data = appointment.comment
                #if form.operationDate.data is None:

                 #   form.operationDate.data = d
                 #   print(type(d))
                 #   print(d)


            print(form.operationDate.data)
            print(form.operationTime.data)

            if form.validate_on_submit():
                print("submit")
                print(type(form.operationDate.data))
                #if form.operationDate.data == d or form.operationTime.data == 1:
                 #   return redirect(url_for('appointment_urgent_modify',id=id))
                appointment.date = form.date.data
                appointment.petType = form.petType.data
                appointment.petName = form.petName.data
                appointment.doctor = form.doctor.data
                appointment.appoint_time = form.appointment_time.data
                appointment.op_date = form.operationDate.data
                appointment.op_time = form.operationTime.data
                appointment.comment = form.comment.data
                db.session.commit()
                return redirect(url_for('My_appointment'))
            else:
                if request.values.get("date"):

                    date = request.values.get("date")
                    appointments = NewAppointment.query.filter(NewAppointment.date == date).all()
                    appointments1 = NewAppointment.query.filter(NewAppointment.op_date == date).all()

                    result_time = {
                        1:"--choose time--",
                        2:"8:00 - 10:00",
                        3:"10:00 - 12:00",
                        4:"13:00 - 15:00",
                        5:"15:00 - 17:00"
                    }
                    #avail_time = [1,2,3,4]
                    for appointment in appointments:
                        if appointment.appoint_time in result_time.keys():
                            result_time.pop(appointment.appoint_time)

                    for appointment1 in appointments1:
                        if appointment1.op_time in result_time.keys():
                            result_time.pop(appointment.appoint_time)

                    return result_time
                return "a"

        else:

            form.applicant.data = appointment.applicant
            date_str = appointment.date
            form.date.data = datetime.date(*map(int,date_str.split('-')))
            form.appointment_time.data = appointment.appoint_time
            form.petType.data = appointment.petType
            form.petName.data = appointment.petName
            form.doctor.data = appointment.doctor
            date_str = appointment.op_date
            if  date_str is not None:
                form.operationDate.data = datetime.date(*map(int,date_str.split('-')))
                form.operationTime.data = appointment.op_time
            form.phoneNo.data = appointment.phoneNo
            form.comment.data = appointment.comment

            return render_template('appointment_urgent_modify.html',form=form,condition=appointment.condition)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('index'))


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
        if appointment.app_type == 1:#普通门诊
            appointment.condition = 5
        else:
            appointment.condition = 3 #预约手术
        db.session.commit()
    elif request.method == 'GET' and request.values.get("type") == "shoushu_d":
        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
        appointment.condition = 4 #开始手术
        db.session.commit()
    elif request.method == 'GET' and request.values.get("type") == "finishOperation":
        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
        appointment.condition = 5 #手术结束
        db.session.commit()
    elif request.method == 'GET' and request.values.get("type") == "makeMedicine":
        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
        appointment.condition = 6 #开药
        db.session.commit()
    elif request.method == 'GET' and request.values.get("type") == "fee":
        appointment = NewAppointment.query.filter(NewAppointment.id == id).first()
        appointment.condition = 7 #缴费
        db.session.commit()


    return render_template('appointment_trace.html',condition=condition,id=id,user_type=session['USERTYPE'],app=app)


#Yiming Sun(2020/3/14)
@app.route('/New_appointment', methods=['GET', 'POST'])
def New_appointment():
    id = session.get("USERNAME")
    img = get_img_path(id)
    form = AppointmentForm()

    #form.select_doctor(session.get("PLACE"))
    if not session.get("USERNAME") is None:

        user = Customer.query.filter(Customer.username == session.get("USERNAME")).first()
        form.applicant.data = user.username
        form.phoneNo.data = user.phone

        #print(form.date.data)
        #print(form.petType.data)
        #print(form.doctor.data)


        if form.validate_on_submit():
            if form.appointment_time.data == 1:
                flash("please choose valid time!")
                return redirect(url_for('New_appointment'))

            name = form.applicant.data
            date = form.date.data
            appoint_time = form.appointment_time.data
            petType = form.petType.data
            doctor = form.doctor.data
            petName = form.petName.data
            phoneNo = form.phoneNo.data
            comment = form.comment.data
            user_id = session.get("USERNAME")
            appointment = NewAppointment(appoint_time=appoint_time,app_type=1,applicant=name,petName=petName,user_id=user_id,date=date,petType=petType,doctor=doctor,phoneNo=phoneNo,comment=comment)
            db.session.add(appointment)
            db.session.commit()
            return redirect(url_for('My_appointment'))
        else:

            if request.values.get("date"):

                date = request.values.get("date")
                appointments = NewAppointment.query.filter(NewAppointment.date == date).all()
                appointments1 = NewAppointment.query.filter(NewAppointment.op_date == date).all()

                result_time = {
                    1:"--choose time--",
                    2:"8:00 - 10:00",
                    3:"10:00 - 12:00",
                    4:"13:00 - 15:00",
                    5:"15:00 - 17:00"
                }
                #avail_time = [1,2,3,4]
                for appointment in appointments:
                    if appointment.appoint_time in result_time.keys():
                        result_time.pop(appointment.appoint_time)

                for appointment1 in appointments1:
                    if appointment1.op_time in result_time.keys():
                        result_time.pop(appointment.appoint_time)

                return result_time

            if request.values.get("type"):
                #print("type")
                #print(request.values.get("type"))
                type = request.values.get("type")
                #print(petT[type])
                doctors = Employee.query.filter(and_(petT[type] == Employee.animal, session.get("PLACE") == Employee.workplace)).all()
                name_list = {}
                for doctor in doctors:
                    name_list[doctor.id] = doctor.username
                #print(name_list)
                return name_list


    return render_template('New_appointment.html', title='Home',form=form, img=img)



#Yiming Sun(2020/3/14)
@app.route('/Urgent_appointment', methods=['GET', 'POST'])
def Urgent_appointment():
    form = UrgentAppointment()

    #form.select_doctor(session.get("PLACE"))
    id = session.get("USERNAME")
    img = get_img_path(id)
    if not session.get("USERNAME") is None:
        user = Customer.query.filter(Customer.username == session.get("USERNAME")).first()
        form.applicant.data = user.username
        form.phoneNo.data = user.phone

        if form.validate_on_submit():
            if form.appointment_time.data == 1 or form.operationTime.data == 1:
                flash("please choose valid time!")
                return redirect(url_for('Urgent_appointment'))
            name = form.applicant.data
            date = form.date.data
            appoint_time = form.appointment_time.data
            petType = form.petType.data
            doctor = form.doctor.data
            petName = form.petName.data
            phoneNo = form.phoneNo.data
            comment = form.comment.data
            #op_date = form.operationDate.data
            op_date = form.operationDate.data.strftime('%Y-%m-%d')
            op_time = form.operationTime.data
            user_id = session.get("USERNAME")
            appointment = NewAppointment(app_type=2, appoint_time=appoint_time, op_time=op_time, op_date=op_date, applicant=name,petName=petName,user_id=user_id,date=date,petType=petType,doctor=doctor,phoneNo=phoneNo,comment=comment)
            db.session.add(appointment)
            db.session.commit()
            return redirect(url_for('My_appointment'))
        else:


            if request.values.get("type"):
                print("type")
                print(request.values.get("type"))
                type = request.values.get("type")
                #print(petT[type])
                doctors = Employee.query.filter(and_(petT[type] == Employee.animal, session.get("PLACE") == Employee.workplace)).all()
                name_list = {}
                for doctor in doctors:
                    name_list[doctor.id] = doctor.username
                #print(name_list)
                return name_list

            elif request.values.get("date"):
                print("date")
                date = request.values.get("date")
                appointments = NewAppointment.query.filter(NewAppointment.date == date).all()
                appointments1 = NewAppointment.query.filter(NewAppointment.op_date == date).all()
                result_time = {
                    1:"--choose time--",
                    2:"8:00 - 10:00",
                    3:"10:00 - 12:00",
                    4:"13:00 - 15:00",
                    5:"15:00 - 17:00"
                }
                #avail_time = [1,2,3,4]
                for appointment in appointments:
                    if appointment.appoint_time in result_time.keys():
                        result_time.pop(appointment.appoint_time)

                for appointment1 in appointments1:
                    if appointment1.op_time in result_time.keys():
                        result_time.pop(appointment.appoint_time)

                return result_time


            elif request.values.get("op_date"):
                date = request.values.get("op_date")
                appointments = NewAppointment.query.filter(NewAppointment.date == date).all()
                appointments1 = NewAppointment.query.filter(NewAppointment.op_date == date).all()
                result_time = {
                    1:"--choose time--",
                    2:"8:00 - 10:00",
                    3:"10:00 - 12:00",
                    4:"13:00 - 15:00",
                    5:"15:00 - 17:00"
                }
                #avail_time = [1,2,3,4]
                for appointment in appointments:
                    if appointment.appoint_time in result_time.keys():
                        result_time.pop(appointment.appoint_time)

                for appointment1 in appointments1:
                    if appointment1.op_time in result_time.keys():
                        result_time.pop(appointment.appoint_time)

                return result_time

    return render_template('Urgent_appointment.html', title='Home',form=form,img=img)

#Yiming Sun(2020/3/14)
@app.route('/My_appointment',methods=['GET','POST'])
def My_appointment():

    if not session.get("USERNAME") is None:
        id = session.get("USERNAME")
        img = get_img_path(id)

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
                    print(session.get("USERID"))
                    items = NewAppointment.query.filter(NewAppointment.user_id == session.get("USERID")).all()
                    print(items)
                else:
                    items = NewAppointment.query.filter(NewAppointment.petName == petName).all()
                data = NewAppointment.to_json(items)
                doc_list = []
                con_list = []
                for d in data:

                    doc_list.append(Employee.query.filter(d['doctor'] == Employee.id).first().username)
                    con_list.append(condition_dict[int(d['condition'])])
                re = []
                re.append(data)
                re.append(doc_list)
                re.append(con_list)
                return json.dumps(re, ensure_ascii=False)

        else:
            my_appointments = NewAppointment.query.filter(NewAppointment.user_id == session.get("USERNAME")).all()
            employees = Employee.query.all()
            doct_list = {}
            for employee in employees:
                doct_list[employee.id] = employee.username

            return render_template('My_appointment.html', img=img, title='Home',my_appointments=my_appointments,petT=petT, condition_dict=condition_dict, doct_list=doct_list,time_dict=time_dict)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('sign_in_c'))




@app.route('/Doc_appointment', methods=['GET', 'POST'])
def Doc_appointment():

    if not session.get("USERNAME") is None:
        id = session.get("USERNAME")
        user_type = session.get("USERTYPE")
        img = get_img_path(id)
        if request.method == "POST":
            id = request.values.get("appointment_id")
            print(id)
            appointment = NewAppointment.query.filter(NewAppointment.id==id).first()
            if appointment.app_type == 1:
                appointment.app_type = 2
            else:
                appointment.app_type = 1
            db.session.commit()
            return str(appointment.app_type)
        else:

            my_e = Employee.query.filter(Employee.username == session.get("USERNAME")).first()
            my_appointments = NewAppointment.query.filter(NewAppointment.doctor == my_e.id).all()
            return render_template('Appointment_doc.html', title='Home', my_appointments=my_appointments,time_dict=time_dict,condition_dict=condition_dict,img=img,user_type=user_type)
    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('index'))


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
            flash('No user found with username: {}'.format(form.username.data))
            return redirect(url_for('sign_in_c'))
        if (check_password_hash(user_in_db.password_hash, form.password.data)):
            session["USERNAME"] = user_in_db.username
            session["USERTYPE"] ='customer'
            session["USERID"] = user_in_db.id
            return redirect(url_for('My_appointment'))
        flash('Incorrect Password')
        return redirect(url_for('sign_in_c'))
    return render_template('sign_in.html', title='Sign In', form=form, form_title="Sign in(Customer)")

@app.route('/login_d', methods=['GET', 'POST'])
def sign_in_d():
    form = LoginForm()
    if form.validate_on_submit():
        doc_in_db = Employee.query.filter(Employee.username == form.username.data).first()
        if not doc_in_db:
            flash('No user found with username: {}'.format(form.username.data))
            return redirect(url_for('sign_in_d'))
        if (check_password_hash(doc_in_db.password_hash, form.password.data)):
            session["USERNAME"] = doc_in_db.username
            session["USERTYPE"] = 'employee'
            return redirect(url_for('Doc_appointment'))
        flash('Incorrect Password')
        return redirect(url_for('sign_in_d'))
    return render_template('sign_in.html', title='Sign In', form=form, form_title="Sign in(Employee)")



@app.route('/Configuration', methods=['GET', 'POST'])
def Configuration():
    if session.get('USERNAME') is not None:
        user_type = session.get("USERTYPE")
        if session.get('USERTYPE') == 'customer':
            user = Customer.query.filter(session.get('USERNAME') == Customer.username).first()
            times = user.times
            form = C_personal_space()

            if form.validate_on_submit():

                user.username = form.username.data
                user.email = form.email.data
                user.phone = form.phone.data
                user.nickname = form.nickname.data
                user.gender = form.gender.data
                user.nationality = form.nationality.data
                user.city = form.city.data
                user.address = form.address.data
                user.personal_signature = form.personal_signature.data
                if form.picture.data is not None:
                    up = Config.UPLOAD
                    file_photo = form.picture.data
                    print(file_photo)
                    print(form.picture)

                    filename = user.username + '.jpg'
                    file_photo.save(os.path.join(up,filename))

                db.session.commit()
                return redirect(url_for('Configuration'))
            else:


                form.username.data = user.username
                form.email.data = user.email
                form.phone.data = user.phone
                form.nickname.data = user.nickname
                form.gender.data = user.gender
                form.nationality.data = user.nationality
                form.city.data = user.city
                form.address.data = user.address
                form.personal_signature.data = user.personal_signature

                #img_path = url_for('static', filename= 'Picture/%s.jpg'%(user.username))
                if os.path.exists('blogapp/static/upload_photo/%s.jpg'%(user.username)):
                    img_path = 'blogapp/static/upload_photo/%s.jpg'%(user.username)
                else:
                    img_path = 'blogapp/static/upload_photo/default.jpg'
                figfile = io.BytesIO(open(img_path,'rb').read())

                img = base64.b64encode(figfile.getvalue()).decode('ascii')


                return render_template('Configuration.html', title='Configuration', form=form,img=img, times=times,user_type=user_type)

        else:
            employee = Employee.query.filter(session.get('USERNAME') == Employee.username).first()
            form = E_personal_space()

            if form.validate_on_submit():

                employee.username = form.username.data
                employee.email = form.email.data
                employee.phone = form.phone.data
                employee.nickname = form.nickname.data
                employee.gender = form.gender.data
                employee.workplace = form.workplace.data
                employee.animal = form.animal.data
                employee.nationality = form.nationality.data
                employee.city = form.city.data
                employee.address = form.address.data
                employee.personal_signature = form.personal_signature.data

                if form.picture.data is not None:
                    up = Config.UPLOAD
                    file_photo = form.picture.data
                    filename = employee.username + '.jpg'
                    file_photo.save(os.path.join(up,filename))

                db.session.commit()


                return redirect(url_for('Configuration'))
            else:

                form.username.data = employee.username
                form.email.data = employee.email
                form.phone.data = employee.phone
                form.animal.data = employee.animal
                form.workplace.data = employee.workplace
                form.nickname.data = employee.nickname
                form.gender.data = employee.gender
                form.nationality.data = employee.nationality
                form.city.data = employee.city
                form.address.data = employee.address
                form.personal_signature.data = employee.personal_signature

                if os.path.exists('blogapp/static/upload_photo/%s.jpg'%(employee.username)):
                    img_path = 'blogapp/static/upload_photo/%s.jpg'%(employee.username)
                else:
                    img_path = 'blogapp/static/upload_photo/default.jpg'
                figfile = io.BytesIO(open(img_path,'rb').read())
                img = base64.b64encode(figfile.getvalue()).decode('ascii')

                return render_template('Configuration.html', title='Configuration', form=form, img=img, user_type=user_type)

    else:
        flash("User needs to either login or signup first")
        return redirect(url_for('login'))


@app.route('/appointment_type/<place>')
def appointment_type(place):
    id = session.get("USERNAME")
    img = get_img_path(id)

    session["PLACE"] = place
    return render_template('appointment_type.html', title="home", img=img)

@app.route('/location_type')
def location_type():
    id = session.get("USERNAME")
    img = get_img_path(id)

    return render_template('location_type.html', title="home", img=img)


@app.route('/signupC', methods=['GET', 'POST'])
def signupC():

    form = SignForm_C()
    if request.method == 'GET':
        return render_template('signupC.html', title="home",form=form)
    if request.method == 'POST':
        customers = Customer.query.all()
        employees = Employee.query.all()
        if request.values.get("type") == "username":
            message = "correct"
            username = request.values.get("username")
            for c in customers:
                if username == c.username:
                    message = "this username has existed!"
                    break
            for c in employees:
                if username == c.username:
                    message = "this username has existed!"
                    break
            return message
        elif request.values.get("type") == "phone":
            message = "correct"
            phone = request.values.get("phone")
            for c in customers:
                if phone == c.phone:
                    message = "this phone has existed!"
                    break
            for c in employees:
                if phone == c.phone:
                    message = "this phone has existed!"
                    break
            return message
        elif request.values.get("type") == "email":
            message = "correct"
            email = request.values.get("email")
            for c in customers:
                if email == c.email:
                    message = "this email has existed!"
                    break
            for c in employees:
                if email == c.email:
                    message = "this email has existed!"
                    break
            return message
        elif request.values.get("type") == "password":
            message = "correct"
            password = request.values.get("password")
            repeat_password = request.values.get("repeat_password")
            if password != repeat_password:
                message = "two password are not consistent"
            return message
        else:
            if form.validate_on_submit():
                flag = True
                username = form.username.data
                password = form.password.data
                repeat_password = form.repeat_password.data
                password_hash = generate_password_hash(password)
                email = form.email.data
                phone = form.phone.data
                nickname = form.nickname.data

                customers = Customer.query.all()
                for c in customers:
                    if username == c.username or phone == c.phone or email == c.email:
                        flag = False
                        break
                if password != repeat_password:
                    flag = False
                if flag:
                    customer = Customer(username=username, password_hash=password_hash, email=email, phone=phone, nickname=nickname)
                    db.session.add(customer)
                    db.session.commit()
                    return redirect(url_for('index'))
                else:
                    flash("message error")
                    return redirect(url_for('signupC'))
            return render_template('signupC.html', title="home",form=form)







@app.route('/signupE', methods=['GET', 'POST'])
def signupE():
    form = SignForm_E()
    if request.method == 'GET':
        return render_template('signupE.html', title="home",form=form)
    if request.method == 'POST':
        customers = Customer.query.all()
        employees = Employee.query.all()
        if request.values.get("type") == "username":
            message = "correct"
            username = request.values.get("username")
            for c in employees:
                if username == c.username:
                    message = "this username has existed!"
                    break
            for c in customers:
                if username == c.username:
                    message = "this username has existed!"
                    break
            return message
        elif request.values.get("type") == "id":
            message = "correct"
            id = request.values.get("id")
            for c in employees:
                if id == c.emid:
                    message = "this id has existed!"
                    break
            ids = Id.query.all()
            print(ids)
            f = False
            for i in ids:
                if i.cid == id:
                    f = True

            if message == "correct":
                if f == False:
                    message = "this id is invalid"
            return message
        elif request.values.get("type") == "phone":
            message = "correct"
            phone = request.values.get("phone")
            for c in employees:
                if phone == c.phone:
                    message = "this phone has existed!"
                    break
            for c in customers:
                if phone == c.phone:
                    message = "this phone has existed!"
                    break
            return message
        elif request.values.get("type") == "email":
            message = "correct"
            email = request.values.get("email")
            for c in employees:
                if email == c.email:
                    message = "this email has existed!"
                    break
            for c in customers:
                if email == c.email:
                    message = "this email has existed!"
                    break
            return message
        elif request.values.get("type") == "password":
            message = "correct"
            password = request.values.get("password")
            repeat_password = request.values.get("repeat_password")
            if password != repeat_password:
                message = "two password are not consistent"
            return message
        else:
            if form.validate_on_submit():
                flag = True
                username = form.username.data
                password = form.password.data
                id = form.id.data
                repeat_password = form.repeat_password.data
                password_hash = generate_password_hash(password)
                email = form.email.data
                phone = form.phone.data
                nickname = form.nickname.data

                if form.animal.data == 1:
                    workplace = "Beijing"
                elif form.animal.data == 2:
                    workplace = "Shanghai"
                else:
                    workplace = "Chengdu"

                if form.animal.data == 1:
                    animal = "Dog"
                else:
                    animal = "Cat"

                employees = Employee.query.all()
                for c in employees:
                    if username == c.username or phone == c.phone or email == c.email or id == c.emid:
                        flag = False
                        break
                if password != repeat_password:
                    flag = False
                if flag:
                    employee = Employee(username=username, emid=id, password_hash=password_hash, email=email, phone=phone, nickname=nickname, animal=animal, workplace=workplace)
                    db.session.add(employee)
                    db.session.commit()
                    return redirect(url_for('index'))
                else:
                    flash("message error")
                    return redirect(url_for('signupE'))
            return render_template('signupE.html', title="home",form=form)




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

@app.route('/question', methods=['POST', 'GET'])
def question():
    un = session.get('USERNAME')
    type = session.get('USERTYPE')

    userC = Customer.query.filter(Customer.username == un).first()
    userE = Employee.query.filter(Employee.username == un).first()
    if userC is not None:

        if os.path.exists('blogapp/static/upload_photo/%s.jpg'%(un)):
            img_path = 'blogapp/static/upload_photo/' + un + '.jpg'
        else:
            img_path = 'blogapp/static/upload_photo/default.jpg'
        figfile = io.BytesIO(open(img_path, 'rb').read())
        img = base64.b64encode(figfile.getvalue()).decode('ascii')

    if userE is not None:
        if os.path.exists('blogapp/static/upload_photo/%s.jpg'%(un)):
            img_path = 'blogapp/static/upload_photo/' + un + '.jpg'
        else:
            img_path = 'blogapp/static/upload_photo/default.jpg'
        figfile = io.BytesIO(open(img_path, 'rb').read())
        img = base64.b64encode(figfile.getvalue()).decode('ascii')
    #         上面冗余用来查找头像
    if request.method == 'GET':

        question_ground = Question.query.filter().all()
        my_question = Question.query.filter(Question.author_name == un).all()
        question_num = len(my_question)
        return render_template('Question.html',question_ground=question_ground,img=img,my_question=my_question,question_num=question_num, type=type)
    else:
        title = request.form.get('title')
        content = request.form.get('content')

        if session.get("USERNAME") is None:
            flash('Please login first')
            return redirect(url_for('index'))
            # question1 = Question(question_title=title, content=content,author_name = 'Anonymous_user')
            # db.session.add(question1)
            # db.session.commit()
            # return redirect(url_for('question'))
        else:
            name=session.get("USERNAME")
            question1 = Question(question_title=title, content=content,author_name=name)
            db.session.add(question1)
            db.session.commit()
            return redirect(url_for('question'))

@app.route('/question_detail/<int:question_id>',methods=['GET','POST'])
def question_detail(question_id):
    un = session.get('USERNAME')

    userC = Customer.query.filter(Customer.username == un).first()
    userE = Employee.query.filter(Employee.username == un).first()
    if userC is not None:

        if os.path.exists('blogapp/static/upload_photo/%s.jpg'%(un)):
            img_path = 'blogapp/static/upload_photo/' + un + '.jpg'
        else:
            img_path = 'blogapp/static/upload_photo/default.jpg'
        figfile = io.BytesIO(open(img_path, 'rb').read())
        img = base64.b64encode(figfile.getvalue()).decode('ascii')

    if userE is not None:
        if os.path.exists('blogapp/static/upload_photo/%s.jpg'%(un)):
            img_path = 'blogapp/static/upload_photo/' + un + '.jpg'
        else:
            img_path = 'blogapp/static/upload_photo/default.jpg'
        figfile = io.BytesIO(open(img_path, 'rb').read())
        img = base64.b64encode(figfile.getvalue()).decode('ascii')

    #         上面冗余用来查找头像


    user2 = Question.query.filter(Question.id == question_id).first().author
    # 问题都是用户Customer提出的
    # print('tttttttttttttttt'+session.get('USERNAME'))
    temp=session.get('USERNAME')
    type=session.get('type')
    if type == 'employee':
        user = Employee.query.filter(Employee.username == temp).first()
    else:
        user = Customer.query.filter(Customer.username == temp).first()
    print('temp' + temp)
    # question_num = len(user2.realquestions)
    # answer_num = len(user2.realanswer)
    # article_num = len(user2.questions)
    # print('user:'+user.username+'gggggggggggg')
    context = {
            'question': Question.query.filter(Question.id == question_id).first(),
            # 'question_num': question_num,
            # 'answer_num': answer_num,
            # 'article_num': article_num
    }
    return render_template('Question_detail.html', user2=user2,user=user,**context,img=img)



@app.route('/add_answer/',methods=['POST'])
def add_answer():
    content=request.form.get('answer_content')
    question_id=request.form.get('question_id')
    answer=AnswerQuestion(content=content)
    name=session.get('USERNAME')
    type=session.get('USERTYPE')

    if type =='employee':
        employee = Employee.query.filter(Employee.username == name).first()
        question=Question.query.filter(Question.id==question_id).first()
        answer.question=question
        answer.author=employee
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('question_detail',question_id=int(question_id)))
    else:
        print('don t have the permission');
        return redirect(url_for('question_detail', question_id=int(question_id)))


@app.route('/delete_answer/',methods=['POST'])
def delete_answer():
    question_id=request.form.get('question_id')
    answer_id=request.form.get('answer_id')
    answer=AnswerQuestion.query.filter(AnswerQuestion.id==answer_id).first()
    db.session.delete(answer)
    db.session.commit()
    return redirect(url_for('question_detail',question_id=int(question_id)))



@app.route('/someone_detail/<username>',methods=['GET','POST'])
def someone_detail(username):
    # print("ssssssssssssssssssss")
    user2=Customer.query.filter(Customer.username==username).first()
    question_num=len(user2.realquestions)
    answer_num=len(user2.realanswer)
    article_num=len(user2.questions)
    context={
        'articles':Question.query.filter(Question.author_id==user2.id).all(),
        'question_num': question_num,
        'answer_num': answer_num,
        'article_num': article_num
    }
    return redirect(url_for('question'))
    # return render_template('Question_detail.html',image=image,user2=user2,user=g.user,touxiang=touxiang,**context)

# @app.route('/getSession/', methods=['GET', 'POST'])
# def getSession():
#     print(session.get('USERNAME'))
#     return session.get('USERNAME')
@app.route('/delete_question/',methods=['POST'])
def delete_question():
    question_id=request.form.get('question_id')

    question=Question.query.filter(Question.id==question_id).first()
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('question'))


@app.route('/password_modify',methods=['GET','POST'])
def password_modify():
    form = modify_password()
    img = get_img_path(session.get("USERNAME"))
    username = session.get("USERNAME")
    customer = Customer.query.filter(Customer.username == username).first()
    employee = Employee.query.filter(Employee.username == username).first()
    if request.method == 'GET':
        return render_template('password_modify.html',form=form,img=img)

    if request.method == 'POST':
        pre = request.values.get("pre_password")
        new1 = request.values.get("new_password")
        new2 = request.values.get("comfirm_password")
        prepre = generate_password_hash(new1)
        if customer is not None:
            if check_password_hash(customer.password_hash, pre):
                print(customer.password_hash)
                print(prepre)
                if new1 == new2:
                    customer.password_hash = prepre
                    db.session.commit()
                    print(customer.password_hash)
                    print(prepre)
                    flash("Password changed successfully")
                    return redirect(url_for('Configuration'))
                else:
                    flash("Two Password are not equal")
                    return redirect(url_for('password_modify'))
            else:
                flash("The previous password is not correct")
                return redirect(url_for('password_modify'))
        if employee is not None:
            if check_password_hash(pre, employee.password_hash):
                if new1 == new2:
                    employee.password_hash = prepre
                    db.session.commit()
                    flash("Password changed successfully")
                    return redirect(url_for('Configuration'))
                else:
                    flash("Two Password are not equal")
                    return redirect(url_for('password_modify'))
            else:
                flash("The previous password is not correct")
                return redirect(url_for('password_modify'))



@app.route('/detail')
def detail():
    return render_template('details.html',title='hh')




@app.route('/user', methods=['POST'])
def check_user():
    userName = request.form['username']
    haveregisted = userInfoTable.query.filter_by(username=request.form['username']).all()
    if haveregisted.__len__() != 0: # 判断是否已被注册
        passwordRight = userInfoTable.query.filter_by(username=request.form['username'],
        password=request.form['password']).all()
        if passwordRight.__len__() != 0:
            print(str(userName) + "log success")
            return '登录成功'
        else:
            return '1'
    else:
        print(str(userName) + "log fail")
        return '0'