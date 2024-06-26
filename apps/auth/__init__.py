#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/26 下午2:40
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from flask import Blueprint
from .forms import LoginForm
from .views import RegisterView,CaptchaView,GraphCaptchaView,LoginView,LogoutView


bp = Blueprint('auth', __name__, url_prefix='/auth')

bp.add_url_rule('/register', view_func=RegisterView.as_view('register'),endpoint='register')
bp.add_url_rule('/captcha', view_func=CaptchaView.as_view('captcha'),endpoint='captcha')
bp.add_url_rule('/graph_captcha', view_func=GraphCaptchaView.as_view('graph_captcha'),endpoint='graph_captcha')
bp.add_url_rule('/login', view_func=LoginView.as_view('login'),endpoint='login')
bp.add_url_rule('/logout', view_func=LogoutView.as_view('logout'),endpoint='logout')


