import pytest


# class TestData:
#     @pytest.mark.parametrize(["a", "b"],[(10, 20),(10, 5),(3, 9)])
#     def test_data(self, a, b):
#         print(a+b)
import yaml


class TestData:
    @pytest.mark.parametrize(["a", "b"],yaml.safe_load(open('./data.yaml')))
    def test_data(self, a, b):
        print(a+b)