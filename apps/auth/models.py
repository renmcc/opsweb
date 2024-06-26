#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/26 下午2:46
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from werkzeug.security import generate_password_hash, check_password_hash
from exts import db
import shortuuid
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _password = db.Column(db.String(200), nullable=False)
    realname = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    join_time = db.Column(db.DateTime, default=datetime.now)
    is_staff = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, *args, **kwargs):
        if "password" in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop("password")
        super(UserModel, self).__init__(*args, **kwargs)
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
    def __str__(self):
        return self.username