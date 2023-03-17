"""
=====================
Author：Tan
Time：2023/3/17 15:36
Project：python学习
=====================
"""


def login_check(username, passwd):
    if username is not None and passwd is not None:
        if username == "tmq" and passwd == "0922":
            return "密码输入正确，登录成功！"
        else:
            return "密码输入错误，登录失败！"
    else:
        return "账号或密码不能为空！！！"
