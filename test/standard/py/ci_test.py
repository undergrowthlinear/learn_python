"""
置信区间
    期望(均值/u)
    标准差=均方差
区间估计可信度更高

参考 https://www.zhihu.com/question/26419030

Z校验值
Z	P值	差异程度
>2.58	<0.01	非常显著
>1.96	<0.05	显著
<1.96	>0.05	不显著
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
print('计算Z校验值')


# 计算置信区间全过程
def cal_z(s1_avg, s1_num, s1_std, s2_avg, s2_num, s2_std):
    di_avg = s1_avg - s2_avg
    s_sum = s1_std * s1_std / s1_num + s2_std * s2_std / s2_num
    return di_avg / math.sqrt(s_sum)


def cal_ci():
    s1_num = 33771
    s1_all = 777193
    s2_num = 34190
    s2_all = 755929
    # 计算均值
    s1_avg = s1_all / s1_num
    s2_avg = s2_all / s2_num
    # 23.013621154244767 22.109651945013162
    print(s1_avg, s2_avg)
    # 根据单个与均值计算
    s1_std = 53.21
    s2_std = 50.21
    z = cal_z(s1_avg, s1_num, s1_std, s2_avg, s2_num, s2_std)
    # 2.27 >1.96	<0.05	显著
    print('z:{}'.format(z))
    # 效果好坏 -0.039 提升为负数 效果差
    d_avg = (s2_avg - s1_avg)
    print('d_avg / s1_avg:{}'.format(d_avg / s1_avg))
    # 差多少 置信空间
    s_sum_sqrt = math.sqrt(s1_std * s1_std / s1_num + s2_std * s2_std / s2_num)
    # -0.9039692092316045 0.3969567052843686 0.7780351423573625
    print(d_avg, s_sum_sqrt, s_sum_sqrt * 1.96)
    # 区间 即区间 [-1.678, -0.122] 有 95%(z=1.96) 查表可得 的可能性包含两个总体均值之差
    print(d_avg - s_sum_sqrt * 1.96, d_avg + s_sum_sqrt * 1.96)
    # 相对比与均值的变化
    print((d_avg - s_sum_sqrt * 1.96) / s1_avg,
          (d_avg + s_sum_sqrt * 1.96) / s1_avg)


cal_ci()
