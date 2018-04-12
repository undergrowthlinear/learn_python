# encoding=utf-8

'''
参考
http://www.runoob.com/python3/python3-reg-expressions.html
\S ----非空白字符
\d ----数字
\u4E00-\u9FD5 ---- 汉字
'''

# 正则测试

import re

text = 'abc123-你好 hello 我'


def re_test(pattern_str, text, is_match=True, flags=0):
    print('text---->{}'.format(text), 'pattern_str---->{}'.format(pattern_str),
          'flags {}'.format(flags), end='\t')
    if is_match:
        result = re.match(pattern_str, text, flags)
    else:
        result = re.search(pattern_str, text, flags)
    if result:
        print('result.group()---->{}'.format(result.group()))
    else:
        print()


def findall_test(pattern_str, text):
    pattern = re.compile(pattern_str, re.U)
    result_l = pattern.findall(text)
    print('text---->{}'.format(text), 'pattern_str---->{}'.format(
        pattern_str), end='\t')
    if result_l:
        for r in result_l:
            print('result_l {}'.format(r), end='\t')
        print()
    else:
        print()


# match ----从头开始匹配 匹配一次
re_test('(\S+)', text)
re_test('[a-zA-Z]*', text, flags=re.I)
re_test('\d+', text, flags=re.I)
# search ----匹配一次 不是从头开始
re_test('\d+', text, is_match=False, flags=re.I)
re_test('hello', text, is_match=False, flags=re.I)
# finaall ----匹配所有 返回列表
# compile ----编译正则,用于search/match/finaall使用
findall_test("[a-zA-Z]+", text)
findall_test("([\u4E00-\u9FD5]+)", text)
