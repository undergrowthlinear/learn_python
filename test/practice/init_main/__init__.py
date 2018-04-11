import sys
'''
如果你希望 python 将一个文件夹作为 Package 对待，那么这个文件夹中必须包含一个名为 __init__.py 的文件，即使它是空的
如果你需要 python 将一个文件夹作为 Package 执行，那么这个文件夹中必须包含一个名为 __main__.py 的文件
对于一个 Package 来说，既然 __init__.py 必须存在，并且当作为模块执行的时候，它会先执行，我们就应该把入口函数 main() 定义在 __init__.py 中。
当我们使用模块方式 -m 执行的时候， __init__.py 定义了 main() 函数，然后在 __main__.py 中调用它，就能实现我们统一入口的目的
'''
print('__init__')
print('__init__.__name__ {}'.format(__name__))
print('__init__.__package__ {}'.format(__package__))

print('sys.path {}'.format(sys.path))
