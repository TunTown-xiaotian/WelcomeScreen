from tokenize import generate_tokens

import jwt
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash

from app.db import execute_sql, query_one



auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "缺少用户名或密码", "code": 400}), 400

    user = query_one("SELECT * FROM users WHERE username = %s", (username,))
    # 本课先用明文密码演示，第 6 节升级为哈希（真实项目严禁明文）
    if not user or generate_password_hash(user["password"]) != password:
        return jsonify({"error": "用户名或密码错误", "code": 401}), 401

    token = jwt.encode(
        {"user_id": user["id"],
         "exp": datetime.now() + timedelta(hours=2)},
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )
    return jsonify({"token": token, "expires_in": 7200})

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"msg": "用户名和密码不能为空"}), 400
    username = data["username"]
    password = data["password"]
    existing = query_one(
        "SELECT id FROM users WHERE username = %s",
        (username,)
    )
    if existing:
        return jsonify({"msg": "用户名已存在"}), 409
    execute_sql(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, generate_password_hash(password))
    )
    return jsonify({"msg": "注册成功"}), 201