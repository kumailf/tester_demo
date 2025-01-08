# login function
def login(username, password):
    # username: str
    # password: int
    # 类型校验
    if not isinstance(username, str):
        return False, "用户名类型错误"
    if not isinstance(password, int):
        return False, "密码类型错误"

    # 登录密码校验
    status, info = login_sql(username, password)
    return status, info


def login_sql(username, password):
    # username: str
    # password: int
    user = {"1": 1, "a": 2}
    if username not in user.keys():
        return False, "用户名不存在"
    elif user[username] != password:
        return False, "密码错误"
    else:
        return True, "登录成功"