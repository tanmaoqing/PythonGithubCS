"""
=====================
Author：Tan
Time：2023/3/17 15:57
Project：python学习
=====================
"""
import pytest

from PytestAndFixtrue.login import login_check

datas = [
    {"username": "tmq", "passwd": "0922", "bei": "密码输入正确，登录成功！"},
    {"username": "ryy", "passwd": "123456", "bei": "密码输入错误，登录失败！"},
    {"username": None, "passwd": None, "bei": "账号或密码不能为空！！！"}
]


class TestLogin:

    @pytest.mark.parametrize("case", datas)
    @pytest.mark.usefixtures("hello")  # 调用fixture函数
    def test_login_success(self, case):
        zhang_hao = login_check(case["username"], case["passwd"])
        assert zhang_hao == case["bei"]

    # def test_login_defeat(self):
    #     zhang_hao = login_check("ryy", "123456")
    #     assert zhang_hao == "密码输入错误，登录失败！"
    #
    # def test_login_null(self):
    #     zhang_hao = login_check(None, None)
    #     assert zhang_hao == "账号或密码不能为空！！！"
