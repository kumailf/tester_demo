import pytest
from api import request_login

@pytest.mark.success
def test_login_success():
    status, info = request_login("1", 1)
    assert status == True
    assert info == "登录成功"

@pytest.mark.failure
def test_login_wrong_password():
    status, info = request_login("1", 2)
    assert status == False
    assert info == "密码错误"

@pytest.mark.failure
def test_login_nonexistent_user():
    status, info = request_login("b", 1)
    assert status == False
    assert info == "用户名不存在"

@pytest.mark.error
def test_login_username_type_error():
    status, info = request_login(1, 1)
    assert status == False
    assert info == "用户名类型错误"

@pytest.mark.error
def test_login_password_type_error():
    status, info = request_login("1", "1")
    assert status == False
    assert info == "密码类型错误"