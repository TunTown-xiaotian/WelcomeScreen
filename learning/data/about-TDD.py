#关于TDD测试驱动开发

#核心思维红-绿-重构三步走
#红red先写测试代码。
#绿green写最少的业务代码
#重构优化代码结构，逻辑，可读性，性能。
#**每增加一个新功能，就重复循环一次**

#测试代码建议安装pytest ，终端运行pytest test_你的文件名.py -v

#测试一个普通函数好的模版



# 1. 导入你要测试的函数
from your_module import your_function

"""
# --------------------------
# 第一类：正常场景测试
# 验证功能在常规输入下是否符合预期
# --------------------------
def test_your_function_normal_case():
    # 给定输入
    input_data = '常规输入'
    # 预期输出
    expected = '预期结果'
    # 执行代码
    result = your_function(input_data)
    # 断言结果
    assert result == expected


# --------------------------
# 第二类：边界场景测试
# 验证极端值、临界值是否处理正确（绝大多数bug出在这里）
# 比如：空值、0、最大值、最小值、第一个/最后一个元素等
# --------------------------
def test_your_function_boundary_case():
    assert your_function('边界值1') == '预期结果1'
    assert your_function('边界值2') == '预期结果2'


# --------------------------
# 第三类：异常场景测试
# 验证错误输入时，是否能正确抛出预期的异常
# --------------------------
def  test_your_function_error_case():
    import pytest
    # 传入非法输入，验证抛出指定异常
    with pytest.raises('预期的异常类型'):
        your_function('非法输入')
"""


"""
# test_calculator.py
from calculator import Calculator

class TestCalculator:
    # 每个测试方法执行前都会运行，用来初始化测试对象
    def setup_method(self):
        self.calc = Calculator()

    # 正常场景
    def test_add_two_numbers(self):
        assert self.calc.add(2, 3) == 5

    # 边界场景
    def test_add_zero(self):
        assert self.calc.add(0, 0) == 0

    # 异常场景
    def test_add_non_number_raises_error(self):
        import pytest
        with pytest.raises(TypeError):
            self.calc.add("a", 3)
"""
