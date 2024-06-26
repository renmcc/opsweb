#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @时间 : 2024/6/21 上午7:26
# @作者 : ren_mcc
# @邮箱 : ren_mcc@foxmail.com

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_caching import Cache
from flask_wtf import CSRFProtect
from flask_avatars import Avatars
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
# from apps.auth.models import *

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache()
csrf = CSRFProtect()
avatars = Avatars()
limiter = Limiter(key_func=get_remote_address,default_limits=['120/minute'])
