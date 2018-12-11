"""
置信区间
    期望(均值/u)
    标准差=均方差
区间估计可信度更高

参考 https://www.zhihu.com/question/26419030
"""
import math
# 两组的平均数都是70，但A组的标准差约为17.08分，B组的标准差约为2.16分，说明A组学生之间的差距要比B组学生之间的差距大得多
a = [95, 85, 75, 65, 55, 45]
b = [73, 72, 71, 69, 68, 67]


def avg(data):
    s = sum(data)
    return s / len(data)


def stand_dev(data):
    d_v = avg(data)
    s = 0
    for d in data:
        s += (d - d_v) * (d - d_v)
    return math.sqrt(s / len(data))


a_v = avg(a)
b_v = avg(b)
print(a_v, b_v)
sd_a = stand_dev(a)
sd_b = stand_dev(b)
print(sd_a, sd_b)
