import logging

from flask_cors import CORS
from flask import Flask
from routes.auth import auth_bp
from utils.validate import validate_bp
from .config import config
from .db import init_db


def create_app(config_name="default"):
    """应用工厂：按需创建、配置 Flask 实例"""
    app = Flask(__name__, static_folder="../static", static_url_path="/")
    app.config.from_object(config[config_name])
    logging.basicConfig(level=logging.INFO,
                        format=
                        "%(asctime)s | %(levelname)-8s "
                       "| %(name)s | %(filename)s:"
                        "%(lineno)d ""| %(message)s",
                filename="app.log")


    init_db(app)
    # CORS(app)

    # 注册蓝图（第 5 节内容）
    from  routes.todos import todos_bp
    app.register_blueprint(validate_bp, url_prefix="/api")
    app.register_blueprint(todos_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api")

    return app