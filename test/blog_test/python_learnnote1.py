# encoding=utf-8

# 列表--list 显示
def list_test(mock_list):
    mock_list = list(mock_list)
    print('*' * 40, 'list_test', '*' * 40)
    print('mock_list format {}'.format(mock_list))
    print('len(mock_list) {}'.format(len(mock_list)))
    mock_list.append(len(mock_list) + 1)
    print('mock_list.append {}'.format(mock_list))
    # 可构造队列(先入先出) 或者 堆栈(先入后出)
    print('mock_list.pop(0) {}'.format(mock_list.pop(0)))
    print('mock_list.pop(-1) {}'.format(mock_list.pop(-1)))
    print('mock_list format {}'.format(mock_list))
    print('mock_list[0:2] {}'.format(mock_list[0:2]))
    print('sorted(mock_list[0:2], reverse=True)  {}'.format(
        sorted(mock_list[0:2], reverse=True)))
    print('*' * 40, 'list_test', '*' * 40)


# 元组 不可修改
def tuple_test():
    mock_tuple = tuple(i for i in range(10) if i % 2 == 0)
    print('*' * 40, 'tuple_test', '*' * 40)
    print('mock_tuple {}'.format(mock_tuple))
    print('len(mock_tuple) {}'.format(len(mock_tuple)))
    print('mock_tuple[0] {}'.format(mock_tuple[0]))
    try:
        mock_tuple[5] = 100
    except TypeError as error:
        print('tuple不能添加元素', error)
    print('*' * 40, 'tuple_test', '*' * 40)


# 词典
def dict_test(mock_dict):
    mock_dict = dict(mock_dict)
    print('*' * 40, 'dict_test', '*' * 40)
    print('mock_dict {}'.format(mock_dict))
    print('mock_dict.keys() {}'.format(mock_dict.keys()))
    print('mock_dict.values() {}'.format(mock_dict.values()))
    for k, v in mock_dict.items():
        print(k, '=', v, end='\t')
    print()
    print('*' * 40, 'dict_test', '*' * 40)


# 集合
def set_test(mock_set):
    mock_set = set(mock_set)
    print('*' * 40, 'set_test', '*' * 40)
    print('mock_set {}'.format(mock_set))
    mock_set.add(0)
    print('mock_set mock_set.add(0) {}'.format(mock_set))
    mock_set.add(100)
    print('mock_set mock_set.add(100) {}'.format(mock_set))
    print('*' * 40, 'set_test', '*' * 40)


# 对于可变参数 分别使用元组(*)与字典(**)进行接收
def func_test(num1, num2, *c, **d):
    print('*' * 40, 'func_test', '*' * 40)
    print('num1({})+num2({}) = {}'.format(num1, num2, num1 + num2))
    print('可变参数使用元组与字典接收 ',c, d)
    print('*' * 40, 'func_test', '*' * 40)
    return (num1, num2, (num1 + num2))


# 使用列表推导式进行初始化 任意类型元素组成的序列,列表可变,用[]表示
list_test([i for i in range(10) if i % 2 == 0])
# 元组 元组不可变,用()表示
tuple_test()
# 字典 {key:value}
dict_test({i: i + 1 for i in range(10) if i % 2 == 0})
# 集合 仅剩下键的词典
set_test({i for i in range(10) if i % 2 == 0})
# 函数
'''
函数----函数是Python的一等公民 函数作为参数/内部函数/闭包/匿名函数lambda()
- 位置参数----根据形参的位置进行参数匹配
- 关键字参数----根据形参的名称进行参数匹配
'''
# 位置参数
func_test(1, 2)
# 关键字参数
first, second, sum = func_test(num2=1, num1=2)
print('f+s=sum', first, second, sum)
# 对于可变参数 分别使用元组(*)与字典(**)进行接收
func_test(5, 10, 100, 200, 300, num3=1000, num4=1000)
