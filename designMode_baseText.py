#!/usr/bin/python3
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


def mainCase():
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

# 面向对象编程的主要概念
# 封装：
'''
    对象的行为对于外部世界来说是不可见的
    对象的状态信息是私密的。
    客户端不能通过直接操作来改变对象的内部状态
    反之：客户端需要通过发送消息来请求对象改变内部状态
    对象根据请求类型，特定成员函数改变其内部状态，与之对应
    注意：如果在变量或函数名前面加上前缀__,就可以将其可访问性变为私有。
'''
'''
多态：
    类型：
        对象根据输入参数提供方法的不同实现
        不同类型的对象可以使用相同的接口
'''


def Polymorphism():
    a = "John"
    b = 1, 2, 3,
    c = [itr for itr in range(14)]
    print(a[1], b[0], c[2])
    print(b)


'''
继承：
    表示一个类可以继承父类的（大部分）功能
    被描述为一个重用基类中定义的功能并允许对原始软件的实现进行独立扩展的选项
    可以利用不同类的对象之间的关系建立层次结构
    python支持多重继承既继承多个基类
'''


class typeBase_A:
    def a_means(self):
        print("a1")


'''
类A是基础类，类B继承了类A的特性。
因此，以类B为对象可以访问类A的方法
'''


class type_B(typeBase_A):
    def b_means(self):
        print("b")


'''
抽象：
    提供了一个简单的客户端接口，通过该接口与类及对象进行交互，并调用该接口中定义的方法
    将内部类的复杂性抽象为一个接口，客户端既不需要知道内部实现了
'''


class Adder:
    def __init__(self):
        self.sum = 0

    # 通过add()方法对类Adder的内部细节进行抽象处理
    def add(self, value):
        self.sum += value


'''
组合：一种将对象或类组合或更复杂的数据结构或软件实现的方法
组合的作用就是：一个对象可用于调用其他模块中的成员函数，这样一来，无需通过继承就可以实现基本功能的跨模块使用
'''


class typeB_basic(object):
    def b(self):
        print("b")
        typeBase_A().a_means()


def main_caseDaily0407():
    objB = typeB_basic()
    objB.b()


def main_tage():
    acc = Adder()
    for i in range(101):
        acc.add(i)
    print(acc.sum)

'''
1.3面向对象设计原则：
    1；开放/封闭原则：类或对象及其方法对于扩展来说，应该是开放的，但是对于修改来说，应该是封闭的
    开发软件应用的时候一定确保通用的方式来编写类或模块，以便当需要扩展类或对象行为的时候不必修改类本身。
    优点：
        现有的类不会被修改，因此退化的可能性较小
        它还有助于保持以前代码的向后兼容性
    定义：软件实体（类、模块、函数等）应该是可以扩展的，但是不可修改的。
    两个主要的特征：
        对于扩展是开放的（open for extension）
        对于修改是封闭的（closed for modification）
'''
if __name__ == '__main__':
    main()
