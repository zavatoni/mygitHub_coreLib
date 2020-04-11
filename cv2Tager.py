#!/usr/bin/python3
import openpyxl
print(dir(openpyxl))

# print(dir(pandas))
'''
设计模式三大类型：
    创建型
    结构型
    行为型
'''
# 理解面向对象编程
'''
对象具有属性(数据成员)和过程(函数)
对象就是类的实例
应用开发：通过让对象交互来实现目标的过程
对象描述：所开发的应用程序内的实体、实体间通过交互来解决现实世界的问题
类：定义对象属性和行为
    属性是数据成员，行为由成员函数表示
    类包含为对象提供初始状态的构造函数
    像模板一样，易于重复使用
方法：对象的行为
    为实现所需的功能，可以对属性进行处理
'''


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        return "<Person ({},{})>".format(self.name, self.age)


def main():
    p = Person("Szz", 31)
    print("Type of object:{}".format(type(p)))
    print("Memory Address:{}".format(id(p)))

'''
面向对象编程的主要概念：
封装的特点：
    对象的行为对于外部世界
'''
# 讨论面向对象设计原则

# 理解设计模式的概念及分类背景

# 讨论动态语言的设计模式

# 设计模式的分类--创建型模式，结构型模式和行为型模式
if __name__ == '__main__':
    main()
