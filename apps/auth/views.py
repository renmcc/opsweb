#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/26 下午2:40
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from flask import Blueprint, render_template, redirect, url_for, flash, current_app,views,request,jsonify,current_app,make_response,session
import string
import random
import time
from io import BytesIO
from hashlib import md5
import re
from exts import mail, cache, db,limiter
from utils import restful
from utils.captcha import Captcha
from .forms import RegisterForm,LoginForm
from .models import UserModel
from middleware.decorators import login_required

class RegisterView(views.MethodView):
    """
    注册视图
    """
    decorators = [limiter.limit('5/minute')]
    def get(self):
        return render_template('register.html')
    def post(self):
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()

            return restful.ok("注册成功")
        else:
            return restful.params_error(form.messages)


class CaptchaView(views.MethodView):
    """
    邮箱验证码视图
    """
    decorators = [limiter.limit('1/minute')]
    def get(self):
        email = request.args.get('email')

        if not email:
            return restful.params_error('请输入邮箱地址')

        rex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(rex, email):
            return restful.params_error('请输入正确格式的邮箱')

        # 6位验证码
        source = list(string.ascii_letters)
        source.extend([str(x) for x in range(0, 10)])
        captcha = ''.join(random.sample(source, 6))

        # celery异步发送验证码
        subject = "[运维管理系统]注册验证码"
        body = f'您的注册验证码为：{captcha}'
        current_app.celery.send_task("send_mail", (email, subject, body))
        # 缓存验证码
        try:
            cache.set(email, captcha)
        except Exception as e:
            print(e)
            return restful.server_error()

        return restful.ok('邮件发送成功')


class GraphCaptchaView(views.MethodView):
    """
        图形验证码视图
    """
    decorators = [limiter.limit('20/minute')]
    def get(self):
        captcha, image = Captcha.gene_graph_captcha()
        # 缓存验证码
        key = md5((captcha+str(time.time())).encode('utf-8')).hexdigest()
        cache.set(key, captcha)

        # 保存验证码到内存
        out = BytesIO()
        image.save(out, 'png')
        # 把 out 文件指针回归最开始位置
        out.seek(0)

        resp = make_response(out.read())
        resp.content_type = 'image/png'

        # 把key放到cookie中，对比时候使用
        resp.set_cookie('_graph_captcha_key', value=key, max_age=3600)
        return resp


class LoginView(views.MethodView):
    """
    登录视图
    """
    decorators = [limiter.limit('10/minute')]
    def get(self):
        return render_template('login.html')
    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                return restful.params_error("邮箱或密码错误")
            if not user.check_password(password):
                return restful.params_error("邮箱或密码错误")
            session['user_id'] = user.id
            if remember == 1:
                # 默认session只要浏览器关闭就消失
                # 配置文件定义7天过期
                session.permanent = True
            return restful.ok('登录成功')
        else:
            return restful.params_error(form.messages)


class LogoutView(views.MethodView):
    """
    登出视图
    """
    decorators = [login_required]
    def get(self):
        session.clear()
        return redirect(url_for('auth.login'))

