#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/26 下午2:55
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from flask import session,g,jsonify,request
from apps.auth.models import UserModel


# 请求 => before_request => 视图函数（返回模板）=> context_processor => context_processor返回的变量也添加到模板中

def admin_before_request():
    if 'user_id' in session:
        user_id = session.get('user_id')
        user = UserModel.query.get(user_id)

        setattr(g, 'user', user)

def admin_context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        return {}

def ratelimit_handler(error):
    print(error)
    return jsonify({"code":400,"message": f"{error}"}), 200