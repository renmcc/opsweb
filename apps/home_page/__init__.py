#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/26 下午3:20
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from flask import Blueprint
from .views import IndexView,HomeView

bp = Blueprint('home_page', __name__, url_prefix='/')

bp.add_url_rule('/', view_func=IndexView.as_view('index'),endpoint='index')
bp.add_url_rule('/home', view_func=HomeView.as_view('home'),endpoint='home')