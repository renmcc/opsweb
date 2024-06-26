#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/26 下午2:44
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from flask_wtf import Form
class BaseForm(Form):
    @property
    def messages(self):
        message_list = []
        if self.errors:
            for errors in self.errors.values():
                message_list.extend(errors)
        return message_list