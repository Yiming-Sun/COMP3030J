import json

from sqlalchemy.orm import Query

from blogapp import db
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    emid = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)
    animal = db.Column(db.String(120), index=True)
    workplace = db.Column(db.String(120), index=True)


class Id(db.Model):
    cid = db.Column(db.String(120), unique=True, primary_key=True)


class NewAppointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant = db.Column(db.String(20), index=True, nullable=False)
    date = db.Column(db.String, index=True, nullable=False)
    petType = db.Column(db.Integer, index=True, nullable=False)
    petName = db.Column(db.String(20), index=True, nullable=False)
    doctor = db.Column(db.Integer, index=True, nullable=False)
    phoneNo = db.Column(db.String(20), index=True, nullable=False)
    comment = db.Column(db.String, default="")
    condition = db.Column(db.Integer, index=True, default=1, nullable=False)
    op_date = db.Column(db.String, index=True)
    op_time = db.Column(db.Integer, index=True)
    app_type = db.Column(db.Integer, index=True)
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
