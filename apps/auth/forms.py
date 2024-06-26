#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/26 下午2:43
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from wtforms import validators,ValidationError,IntegerField
from wtforms.fields import StringField, PasswordField
from wtforms.validators import Email, InputRequired
from wtforms.validators import Length, EqualTo
from .models import UserModel
from exts import cache
from flask import request
from apps.base.forms import BaseForm

class RegisterForm(BaseForm):
    email = StringField('Email', validators=[validators.input_required(message='邮箱不能为空'), validators.Email(message='请输入正确的邮箱')])
    email_captcha = StringField('Email Captcha', validators=[validators.InputRequired(message='邮箱验证码不能为空'),Length(6,6, message="请输入正确的邮箱验证码")])
    username = StringField('Username', validators=[validators.InputRequired(message='用户名不能为空'), validators.Length(min=3, max=20, message="用户名3-20歌字符")])
    password = PasswordField('Password', validators=[validators.InputRequired(message='密码不能为空'),Length(6,20, message='密码6-20个字符')])
    repeat_password = PasswordField("repeat_password",validators=[EqualTo("password", message="两次密码不一致")])
    graph_captcha = StringField('Graph Captcha', validators=[validators.InputRequired(message='图形验证码不能为空'), Length(6,6, message="请输入正确的图形验证码")])

    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise ValidationError(message="邮箱已经被注册")

    def validate_email_captcha(self, field):
        email_captcha = field.data
        email = self.email.data
        cache_captcha = cache.get(email)
        if not cache_captcha or str(email_captcha).lower() != str(cache_captcha).lower():
            raise ValidationError(message="邮箱验证码错误")

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        key = request.cookies.get('_graph_captcha_key')
        cache_captcha = cache.get(key)
        if not cache_captcha or str(graph_captcha).lower() != str(cache_captcha).lower():
            raise ValidationError(message="图形验证码错误")

    def validate_username(self, field):
        new_username = field.data
        username = UserModel.query.filter_by(username=new_username).first()
        if username:
            raise ValidationError('用户名已经存在')


class LoginForm(BaseForm):
    email = StringField('Email', validators=[Email(message="请输入正确的邮箱"),InputRequired(message='邮箱不能为空')])
    password = PasswordField('password', validators=[Length(6,20, message='密码长度6-20个字符'), InputRequired(message="密码不能为空")])
    graph_captcha = StringField('Graph Captcha', validators=[validators.InputRequired(message='图形验证码不能为空'),
                                                             Length(4, 4, message="请输入正确的图形验证码")])
    remember = IntegerField('remember')

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        key = request.cookies.get('_graph_captcha_key')
        cache_captcha = cache.get(key)
        if not cache_captcha or str(graph_captcha).lower() != str(cache_captcha).lower():
            raise ValidationError(message="图形验证码错误")