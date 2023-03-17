"""
=====================
Author：Tan
Time：2023/3/17 11:40
Project：python学习
=====================
"""
import pytest


@pytest.fixture()
def login():
    print('登录操作')
    yield
    print('退出登录')


def test_01(login):
    print('需要用到登录！')


def test_02():
    print('不需要登录！')


def test_03(login):
    print('这里需要用到登录！')
