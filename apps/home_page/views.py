#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/26 下午3:21
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from flask import views,render_template
from middleware.decorators import login_required

class IndexView(views.MethodView):
    """
    索引页视图
    """
    decorators = [login_required]
    def get(self):
        return render_template("index.html")


class HomeView(views.MethodView):
    """
    首页视图
    """
    decorators = [login_required]
    def get(self):
        return render_template("modules/home_page.html")