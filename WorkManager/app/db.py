import os
import pymysql
from dbutils.pooled_db import PooledDB
from flask import current_app


# 进程启动时创建池子（不是每请求创建）
def init_db(app):
    app.extensions["db_pool"] = PooledDB(
        creator=pymysql,
        maxconnections=10,
        host=app.config["DB_HOST"],
        password=app.config["DB_PASSWORD"],
        user=app.config["DB_USER"],
        database=app.config["DB_NAME"],
        port=int(app.config["DB_PORT"]),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def get_connection():
    pool = current_app.extensions["db_pool"]
    return pool.connection()   # 从池中取，用完归还



# query_all / query_one / execute_sql 的代码一行不用改！

def query_all(sql, params=None):
    """查询多条，返回字典列表"""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()
    finally:
        conn.close()

def query_one(sql, params=None):
    """查询多条，返回字典列表"""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()
    finally:
        conn.close()


def execute_sql(sql, params=None):
    """执行增删改，返回影响行数"""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            rows = cur.execute(sql, params)
            conn.commit()      # 写操作必须提交
            return rows
    finally:
        conn.close()