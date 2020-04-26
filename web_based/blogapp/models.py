import json
from sqlalchemy.orm import Query
from datetime import datetime
from blogapp import db
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)
    nickname = db.Column(db.String(20), index=True)
    gender = db.Column(db.Integer, index=True)
    city = db.Column(db.String(10), index=True)
    address = db.Column(db.String(120), index=True)
    nationality = db.Column(db.String(120), index=True)
    personal_signature = db.Column(db.String(120), index=True)
    times = db.Column(db.Integer, index=True, default=0)
    log_con = db.Column(db.Integer,index=True, default=0)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    emid = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)
    animal = db.Column(db.String(120), index=True)
    workplace = db.Column(db.String(120), index=True)
    nickname = db.Column(db.String(20), index=True)
    gender = db.Column(db.Integer, index=True)
    city = db.Column(db.String(10), index=True)
    address = db.Column(db.String(120), index=True)
    nationality = db.Column(db.String(120), index=True)
    personal_signature = db.Column(db.String(120), index=True)
    times = db.Column(db.Integer, index=True, default=0)
    log_con = db.Column(db.Integer, index=True, default=0)


    def to_dict(self):

        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result


class Id(db.Model):
    cid = db.Column(db.String(120), unique=True, primary_key=True)

# 发布的问题
class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_name = db.Column(db.String(64), db.ForeignKey('customer.username'))
    author = db.relationship('Customer', backref=db.backref('realquestions'))


# 针对发布的问题进行的回答
class AnswerQuestion(db.Model):
    __tablename__ = 'answer_question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    answer_question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    author = db.relationship('Employee', backref=db.backref('realanswer'))
    question = db.relationship('Question', backref=db.backref('questionAnswer'))

class NewAppointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant = db.Column(db.String(20), index=True, nullable=False)
    date = db.Column(db.String(20), index=True, nullable=False)
    appoint_time = db.Column(db.Integer, index=True, nullable=False)
    petType = db.Column(db.Integer, index=True, nullable=False)
    petName = db.Column(db.String(20), index=True, nullable=False)
    doctor = db.Column(db.Integer, index=True, nullable=False)
    phoneNo = db.Column(db.String(20), index=True, nullable=False)
    comment = db.Column(db.String(20), default="")
    condition = db.Column(db.Integer, index=True, default=1, nullable=False)
    op_date = db.Column(db.String(20), index=True)
    op_time = db.Column(db.Integer, index=True)
    app_type = db.Column(db.Integer, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    cus_appoint = db.relationship('Customer', backref=db.backref('Customer'))

    def to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    def to_json(all_vendors):
        v = [ven.to_dict() for ven in all_vendors]
        return v


class AlchemyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        # 判断是否是Query
        if isinstance(obj, Query):
            # 定义一个字典数组
            fields = []
            # 检索结果集的行记录
            for rec in obj:
                # 定义一个字典对象
                print(rec)
                record = {}
                # 检索记录中的成员
                for field in rec:
                    print(field)
                    try:
                        record[field] = rec.__getattribute__(field)
                    except TypeError:
                        record[field] = None
                fields.append(record)
            # 返回字典数组
            return fields
        # 其他类型的数据按照默认的方式序列化成JSON
        return json.JSONEncoder.default(self, obj)





