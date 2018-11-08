# coding :utf8
import math
import time


def cal_hour(time_str):
    time_array = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_array))
    now_stamp = int(time.time())
    # 防止出现时间不一致
    if time_stamp > now_stamp:
        now_stamp = time_stamp
    # 距离现在的小时数
    return round((now_stamp - time_stamp) / 3600, 1)


# http://www.ruanyifeng.com/blog/2012/02/ranking_algorithm_hacker_news.html
# score=(p-1)/(t+2) pow G
def cal_hacker_new(hour, like, g=1.8):
    mole = like - 1
    if like == 0:
        mole = 0
    return mole / math.pow(hour + 2, g)


# http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_stack_overflow.html
# (log(10,viewCount)*4+commentCount/5)/(t+1) pow G
def cal_stack_overflow(pv, cc, hour, g=1.5):
    mole = (math.log10(pv)) * 4 + cc / 5
    return mole / math.pow(hour + 1, g)


def main():
    f = open("E:\\iyourcar\\project\\server-services-bdbox\\sql"
             "\\article_pv_cc_fa_50000.csv", 'r', encoding='utf8')
    f_out = open(
        "E:\\iyourcar\\project\\server-services-bdbox\\sql"
        "\\f_pv_cc_fa_50000_out"
        ".csv", 'w',
        encoding='utf8')
    for line in f:
        line = line.strip()
        l_ar = line.split(",")
        if len(l_ar) != 6:
            continue
        id = l_ar[0]
        title = l_ar[1]
        time_str = l_ar[2]
        # view
        pv = int(l_ar[3])
        # comment count
        cc = int(l_ar[4])
        # like
        fa = int(l_ar[5])
        hour = cal_hour(time_str)
        score_hacker_new = cal_hacker_new(hour, fa, 1.8)
        score_stack_overflow = cal_stack_overflow(pv, cc, hour, 1.5)
        line_out = line + "," + '{:.8f}'.format(
            score_hacker_new) + "," + '{:.8f}'.format(
            score_stack_overflow) + "\n"
        f_out.write(line_out)
    f_out.close()
    f.close()


if __name__ == '__main__':
    main()
