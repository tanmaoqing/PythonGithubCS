"""
=====================
Author：Tan
Time：2023/3/20 15:32
Project：python学习
=====================
"""
import pytest


@pytest.fixture()
def hello():
    print("这是前置！")
    yield
    print("这是后置")
