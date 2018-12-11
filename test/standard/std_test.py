"""
python缩进对齐组织代码的执行，所有没有缩进的代码，都会在载入时自动执行

"""
# s = False
s = None
stopwords = [12, 2, 4] if s is not None else [1, 2, 3, 4]
print(stopwords)

import os
# 交互式环境未定义 __file__ 当前脚本运行的路径 E:/java_other/python/code/learn_python/test/standard
print(os.path.dirname(__file__))
# 当文件是被调用时，__name__的值为模块名 当文件被执行时，__name__的值为 ‘__main__’ __main__
print(__name__)
# 当前文件描述
print(__doc__)