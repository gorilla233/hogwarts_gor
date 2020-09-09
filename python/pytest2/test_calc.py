import pytest

from python.pytest2.calculator import Calculator

"""
pytest命名规则
文件名：以test_开头
类名:以Test开头
方法名：test_开头
"""
class TestCalculator:
    def setup_class(self):
        self.calc = Calculator()
        print("\nleifangfa:setupclass")
    def teardown_class(self):
        print("\nleifangfa:teardownclass")

    def setup(self):
        print("开始计算!")
        # self.calc = Calculator()
        # print("setup: 测试用例前的准备")
    def teardown(self):
        print("\n结束计算！")
        # print("\nteardown: 测试用例后的资源释放")

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect',[
        (1, 3, 4),
        (2, 1, 3),
        (0, 1, 1)
    ])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert expect == result

    # @pytest.mark.add
    # def test_add2(self):
    #     result = self.calc.add(3, 5)
    #     assert 8 == result

    # @pytest.mark.add
    # def test_add3(self):
    #     result = self.calc.add(1, 1)
    #     assert 2 == result

    @pytest.mark.div
    @pytest.mark.parametrize('a, b, expect', [
        (3, 3, 1),
        (2, 1, 2),
        (0, 1, 0)
    ])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert expect == result

    # @pytest.mark.div
    # def test_div2(self):
    #     result = self.calc.div(2, 1)
    #     assert 1 == result

"""
模块相当于一个python文件
"""