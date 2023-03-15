"""
=====================
Author：Tan
Time：2023/2/9 17:09
Project：python学习
=====================
"""
from PythonTest.pytest2 import Test

# print("python学习！")
a = "DSSDSWSFW" + "sacrilege"

# print(a)
number = 10
# number_one = 3
number += 10

# salary = input("请输入：")
# salary = int(salary)
# salary1 = input("请输入：")
# set = int(salary) == 50 and salary1 == "好的"
# set1 = not (salary == 60)
# print(salary[1])
# print(salary[len(salary) - 1])
# print(salary[-1])
# print(salary[1:2])
# print(salary[:3])
# print(salary[1:])
# print((salary[::-1]))
# print(salary[::1])

# str_name = "PYthon 学习"
# print(str_name.lower())
# print(a.lower())
# print(str_name.upper())
# print(a.find("sa", 1))
# print(a.upper().find("A"))
# print(a.replace("sacrile", "TTT", 1))
# print(len(a))
# print(str_name.find("的"))


# age = input("请输入：")
# weight = float(input("请输入："))
# print("年龄为：{}，重量为：{}".format(age, "不知道"))
# print("年龄为：{}，重量为：{:.2%}".format(age, weight))
# print(f"年龄为：{8}，重量为：{8*8}".format(age, weight))


# lie = ["11"]
# lie1 = ["小王", "小任"]
# print(lie1.index("小任"))
# print(lie1.append("笑谈"))
# print(lie1[::1])
# print(len(lie1))
# lie1.insert(1, "小孙")
# print(lie1)
# print(lie1.extend(lie))
# lie2 = []
# lie3 = []
# lie2.append(lie1[0])
# lie3.append(lie1[1])
# lie3.extend(lie2)
# print(lie3)
# print(lie1)
# lie1.remove("小王")
# print(lie1)
# del lie1[1]
# print(lie1)
# lie1.pop(0)
# print(lie1)
# dd = ["a", ["d", "r"]]
# dd.pop(0)
# print(dd)

# yuan = ["小", "任", "真", "狗"]
# if "真" not in yuan:
#     print("存在")
# else:
#     print("不存在")
#
# shu = [1, 23, 23, 12, 1, 242, 42, 1321, 3, 242, 423, 1, 24, 24]
# shu.sort()
# print(shu)
# # shu.sort(reverse=True)
# # print(shu)
# shu1 = sorted(shu, reverse=True)
# shu.reverse()
# print(shu1)
# print(shu)
# shu5 = "1, 23, 23, 12, 1, 242, 42, 1321, 3, 242, 423, 1, 24, 24"
# print(shu5.split(","))


# project = {"age": 20, "city": "长沙", "sex": "男"}
# print(project["age"])
# print(project.keys())
# print(project.values())
# print(project.get("age"))
# project["name"] = "小任"
# print(project)
# project.setdefault("hhh", "ddd")
# print(project)
#
# del project["age"]
# print(project)
#
# print(project.items())
# print("hhh" in project)
# print("name" in project.keys())
# print("小任" in project.values())

# money = int(input("请输入金额："))
# if money >= 1000:
#     print("好多啊!")
# elif 1000 > money >= 300:
#     money += 1000
#     print("挺多的!")
#     print(money)
# else:
#     print("好少啊!")
#
# while money:
#     if money == 5:
#         print("555")
#         break
#     elif money == 4:
#         print("444")
#         break
#     elif money == 3:
#         print("333")
#         break
#     else:
#         print("结束")
#         break

# zi = "Hello World"
# for i in range(100):
#     i += 1
#     if i < 50:
#         print("第", i, "个：", zi)
#     elif i == 50:
#         print("结束")
#         break
#     else:
#         print("太大了")
# else:
#     pass


# for i in range(1, 10):
#     for k in range(1, 10):
#         if k < i:
#             print(i, "*", k, "=", i * k, end="\t")
#         elif k == i:
#             print(i, "*", k, "=", i * k, '''''')


# for i in range(1, 10):
#     for k in range(1, 10):
#         if k < i:
#             print(f"{i}*{k}={i * k}", end="\t")
#         elif k == i:
#             print(f"{i}*{k}={i * k}")


pai_xu = [23, 53, 13, 232, 42, 1214, 24]

# def pai_xu_one():
#     for j in range(1, len(pai_xu)):
#         print("jjjj:{}".format(j))
#         print("len(pai_xu):{}".format(len(pai_xu)))
#         print("=======================================================")
#         for i in range(0, len(pai_xu) - j):
#             print("iiiii:{}".format(j))
#             print("len(pai_xu):{}".format(len(pai_xu) - j))
#             if pai_xu[i] > pai_xu[i + 1]:
#                 zhi = pai_xu[i + 1]
#                 pai_xu[i + 1] = pai_xu[i]
#                 pai_xu[i] = zhi
#     print(pai_xu)
#
#
# pai_xu_one()


# shu_zu = [23, 6, 3, 2, 7, 23, 86, 34, 2, 23243]
# for i in range(1, len(shu_zu)):
#     for j in range(0, len(shu_zu) - i):
#         if shu_zu[j] > shu_zu[j + 1]:
#             shu_zu[j], shu_zu[j + 1] = shu_zu[j + 1], shu_zu[j]
# print(shu_zu)

# shu_zu = [23, 6, 3, 2, 7, 7, 86, 34, 2, 23]
# try:
#     a = set(shu_zu)
#     print(a[1])
# except Exception as e:
#     print("有问题")


tt = Test()
tt.test_name("牛肉")
tt.my_eat

# --------------------------


