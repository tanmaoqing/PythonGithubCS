"""
=====================
Author：Tan
Time：2023/3/16 17:04
Project：python学习
=====================
"""
import random

shu_zu = random.randint(1, 10)


def test_case1():
    tt = 9
    print("1、随机数字是：{}".format(shu_zu))
    assert tt == shu_zu


def test_case2():
    print("2、随机数字是：{}".format(shu_zu))
    assert 8 == shu_zu

