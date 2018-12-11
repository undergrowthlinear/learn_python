"""
legb----LEGB就是用来规定命名空间查找顺序的规则
LEGB规定了查找一个名称的顺序为：local-->enclosing function locals-->global-->builtin
L-Local(function)；函数内的名字空间
E-Enclosing function locals；外部嵌套函数的名字空间(例如closure)
G-Global(module)；函数定义所在模块（文件）的名字空间
B-Builtin(Python)；Python内置模块的名字空间

参考 https://www.jianshu.com/p/3b72ba5a209c
"""
# encoding: utf-8

x = 1

def foo():
    x = 2
    def innerfoo():
        x = 3
        print('locals ', x)
    innerfoo()
    print('enclosing function locals ', x)

foo()
print('global ', x)