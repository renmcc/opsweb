#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/23 下午12:36
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from functools import wraps
from flask import g,redirect,url_for,current_app
def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if hasattr(g, 'user'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))
    return wrap

