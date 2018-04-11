# encoding=utf-8

import threading
import time


class myThread(threading.Thread):
    def __init__(self, name=None, delay=1):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        self.func_thread_test(self.name, self.delay)

    # 定义线程函数
    def func_thread_test(self, name, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print('name {} delay {} count {}'.format(name, delay, count))


# 创建线程
try:
    t1 = myThread('t1', 2)
    t2 = myThread('t2', 4)
    t1.start()
    t2.start()
    print('等待线程执行完成,激活线程数目', threading.active_count())
    t1.join()
    t2.join()
    print('执行完所有线程,激活线程数目', threading.active_count())
except Exception as e:
    print(e)

'''
while 1:
    pass
'''
