# server/todos_server.py
from flask import request, jsonify

# 假设你的 query_one 和 execute_sql 在 utils 或其他地方
from app.db import query_one, execute_sql
def delete_todo(todos_id: int) -> tuple[bool, str]:
    """
    处理删除任务的业务逻辑
    返回: (是否成功, 提示信息)
    """
    # 1. 根据id查询任务是否存在
    todo = query_one("SELECT id FROM todos WHERE id = %s", (todos_id,))
    if not todo:
        return False, "任务不存在"
    # 2. 执行删除sql
    execute_sql("DELETE FROM todos WHERE id = %s", (todos_id,))
    return True, "删除成功"

def modify(todos_id):
    data = request.get_json()
    # 判断有没有传json、title字段
    if not data or "title" not in data:
        return jsonify({"error": "title字段不能为空"}), 400
    title = data["title"].strip()
    if not title:
        return jsonify({"error": "title不能是空字符串"}), 400
    if len(title) > 200:
        return jsonify({"error": "title不能超过200字符"}), 400
    # 先查这条任务是否存在
    todo = query_one("SELECT id FROM todos WHERE id = %s", (todos_id,))
    if not todo:
        return jsonify({"msg": "任务不存在"}), 404
    # 可选校验：不能修改成和别的任务重名（如果你需要这个规则）
    same_title = query_one(
        "SELECT id FROM todos WHERE title = %s AND id != %s",
        (title, todos_id))
    if same_title:
        return jsonify({"msg": "该任务名称已存在"}), 409
    # 更新，created_at一般不修改，只更新title
    execute_sql(
        "UPDATE todos SET title = %s WHERE id = %s",
        (title, todos_id)
    )
    return jsonify({"msg": "任务修改成功"}), 200

def create():
    data = request.get_json()
    # 校验是否传了json、是否有title字段
    if not data or "title" not in data:
        return jsonify({"error": "字段 title 不能为空"}), 400
    title = data["title"].strip()
    if not title:
        return jsonify({"error": "title 不能是空字符串"}), 400
    if len(title) > 200:
        return jsonify({"error": "title 字符不能超过200"}), 400
    # 查询是否已有同名任务
    existing = query_one(
        "SELECT id FROM todos WHERE title = %s",
        (title,)
    )
    if existing:
        return jsonify({"msg": "任务已存在"}), 409
    #插入到 todos 表，只插入 title，对应一个 %s
    execute_sql(
        "INSERT INTO todos (title) VALUES (%s)",
        (title,)
    )
    return jsonify({"msg": "任务创建成功"}), 201