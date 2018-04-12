import jieba

seg_list = jieba.cut("他来到了网易杭研大厦")
print(", ".join(seg_list))


def gene_test():
    for i in range(100):
        yield i


def yield_test():
    print('first yield')
    yield 1
    print('second yield')
    yield 2
    print('third yield')
    yield 3
    print('no more yield')

def print_yield_test(li):
    for l in li:
        print(l)

l = gene_test()
print_yield_test(l)

l = yield_test()
print_yield_test(l)
