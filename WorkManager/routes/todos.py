from flask import Blueprint, request, jsonify,g
from app.db import query_all, query_one, execute_sql
from server.todos_server import delete_todo
from utils.auth import login_required

todos_bp = Blueprint("todos", __name__)

@todos_bp.route("todos",methods=["GET"])#我的任务列表
@login_required
def get_todo_list(keyword: str = None):
    """
    获取任务列表，支持可选的关键字搜索
    """
    if keyword:
        todos = query_all(
            "SELECT * FROM todos WHERE user_id = %s AND title LIKE %s",
            (g.current_user_id, f"%{keyword}%")
        )
    else:
        todos = query_all(
            "SELECT * FROM todos WHERE user_id = %s",
            (g.current_user_id,)
        )
    return todos


@todos_bp.route("todos", methods=["POST"])# 新增任务
@login_required
def create_todo():
    """
    处理创建任务的业务逻辑
    返回: (状态码, 提示信息)
    """
    data = request.get_json()
    title = data.get("title","")
    # 查询是否已有同名任务
    existing = query_one(
        "SELECT id FROM todos WHERE title = %s",
        (title,)
    )
    if existing:
        return jsonify({"message":"任务已存在"}), 409
    # 插入到 todos 表，只插入 title
    effect_rows = execute_sql(
        "INSERT INTO todos (user_id,title) VALUES (%s,%s)",
        (g.current_user_id,title)
    )
    if effect_rows:
        return jsonify({"message": "create success"}), 200
    return jsonify({"message": "create failure"}), 500



@todos_bp.route("todos/<int:todos_id>", methods=["PUT"])#修改任务
@login_required
def modify(todos_id: int) -> tuple[int, str]:
    """
    处理修改任务的业务逻辑
    返回: (状态码, 提示信息)
    """
    data = request.get_json()
    completed = data.get("completed", False)
    # 先查这条任务是否存在
    todo = query_one("SELECT id FROM todos WHERE id = %s", (todos_id,))
    if not todo:
        return 404, "任务不存在"
    # 执行更新
    execute_sql(
        "UPDATE todos SET completed = %s WHERE id = %s",
        (completed, todos_id)
    )
    return jsonify({"message": "任务修改成功"}), 200


@todos_bp.route("todos/<int:todos_id>",methods=["DELETE"])#删除任务
@login_required
def delete(todos_id):
    # 调用 server 层的业务逻辑
    success, msg = delete_todo(todos_id)
    if not success:
        return jsonify({"msg": msg}), 404
    # 204 No Content：删除成功，不返回响应内容
    return "", 204

