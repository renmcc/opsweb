#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/21 上午7:25
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

import os
from datetime import timedelta

# 项目根路径
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG=True
TEMPLATES_AUTO_RELOAD = True
# 数据库的配置变量
HOSTNAME = "192.168.10.10"
PORT = 3306
DATABASE = "renbbs"
USERNAME = 'root'
PASSWORD = '910202'
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SERVER_NAME = 'hy.com:5000'
SECRET_KEY = os.urandom(24)
# session过期时间
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# cms userid key
CMS_USER_ID = '1234QWERSQE2D22FDW1'

# 发邮件
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '587'
#MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = ''

# Celery配置
CELERY_BROKER_URL = 'redis://:910202@localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://:910202@localhost:6379/1'

# Cache用redis
CACHE_TYPE = 'RedisCache'
CACHE_DEFAULT_TIMEOUT = 300
CACHE_REDIS_URL = 'redis://:910202@localhost:6379/2'

# 头像
AVATARS_SAVE_PATH = os.path.join(BASE_DIR, 'media/avatars')
POST_IMAGE_SAVE_PATH = os.path.join(BASE_DIR, 'media/post')

# 分页
PER_PAGE_COUNT = 5