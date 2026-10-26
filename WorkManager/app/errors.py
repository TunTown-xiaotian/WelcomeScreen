from flask import jsonify

def register_error_handlers(app):
    """在工厂里调用，统一注册错误处理"""

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "资源不存在", "code": 404}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"error": "请求方法不允许", "code": 405}), 405

    @app.errorhandler(Exception)
    def internal_error(error):
        app.logger.error(f"服务器错误: {error}")  # 记录日志
        return jsonify({"error": "服务器内部错误", "code": 500}), 500