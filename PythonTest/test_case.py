"""
=====================
Author：Tan
Time：2023/3/16 17:04
Project：python学习
=====================
"""
import random

shu_zu = random.randint(1, 10)


def test_cs():
    tt = 9
    print("1、随机数字是：{}".format(shu_zu))
    assert tt == 9


def test_cs1():
    print("2、随机数字是：{}".format(shu_zu))
    assert 8 == shu_zu

