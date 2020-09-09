import pytest

test_user_data = ['Tom','Jerry','CaiXin']
@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 登录用户：{user}")
    return user

@pytest.mark.parametrize('login_r', test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中的返回值：{a}")
    assert a!=''