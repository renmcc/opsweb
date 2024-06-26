from flask import Flask
import config
from exts import db,migrate,mail,cache,csrf,avatars,limiter
from apps.auth import bp as auth_bp
from apps.home_page import bp as home_bp
from apps.media import bp as media_bp
from bbs_celery import make_celery
from middleware.hooks import admin_before_request,admin_context_processor,ratelimit_handler

app = Flask(__name__)
# 加载配置
app.config.from_object(config)
# 初始化数据库
db.init_app(app)
# 初始化migrate
migrate.init_app(app, db)
# 初始化邮件
mail.init_app(app)
# 初始化缓存
cache.init_app(app)
# 初始化celery异步服务
mycelery = make_celery(app)
# 初始化跨域保护
csrf.init_app(app)
# 初始化头像插件
avatars.init_app(app)
# 限速
limiter.init_app(app)

# 初始化钩子函数
app.before_request(admin_before_request)
app.context_processor(admin_context_processor)
app.errorhandler(429)(ratelimit_handler)

# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(media_bp)


if __name__ == '__main__':
    app.run(debug=True,port=6000,host='0.0.0.0')
