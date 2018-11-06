# coding :utf8
# author linxinzhu from https://blog.csdn.net/Season_For_Lin/article/details/78568991
import sys

import jieba

# 11144
i = 0
count = 0
f = open("E:\\java_other\\python\data\\fasttext_test\\series_rela"
         "\\tmp_dwd_base_article_carseriesname.txt", 'r', encoding='utf8')
f_carseriesname_count = open(
    "E:\\java_other\\python\data\\fasttext_test\\series_rela"
    "\\carseriesname_count.txt", 'r', encoding='utf8')
f_carseriesname_count_filter = open(
    "E:\\java_other\\python\\install_package\\fasttext-win64"
    "-latest-Release\\Release\\f_carseriesname_count_filter.txt", 'w',
    encoding='utf8')
outf_train = open("E:\\java_other\\python\\install_package\\fasttext-win64"
                  "-latest-Release\\Release\\train.txt", 'w', encoding='utf8')
outf_test = open("E:\\java_other\\python\\install_package\\fasttext-win64"
                 "-latest-Release\\Release\\test.txt", 'w', encoding='utf8')
series_set = set()
series_filter_set = set()

for line in f_carseriesname_count:
    line = line.strip()
    l_ar = line.split("\001")
    if len(l_ar) != 2:
        continue
    series = l_ar[0]
    num = int(l_ar[1])
    if num < 5:
        continue
    series_set.add(series)
    series_filter_set.add(line)

for line in f:
    line = line.strip()
    l_ar = line.split("\001")
    if len(l_ar) != 4:
        continue
    id = l_ar[0]
    title = l_ar[2]
    content = l_ar[3]
    lable = l_ar[1]
    if lable in series_set:
        l_lable = lable.split(",")
        lable = l_lable[0].split(" ")[0]
        seg_title = jieba.cut(title.replace("\t", " ").replace("\n", " "))
        seg_content = jieba.cut(content.replace("\t", " ").replace("\n", " "))
        outline = " ".join(seg_title) + " " + " ".join(seg_content)
        outline = outline + "\t" + "__label__" + lable + "\n"
        if i < 8000:
            outf_train.write(outline)
        else:
            outf_test.write(outline)

        if i % 2500 == 0:
            count = count + 1
            sys.stdout.flush()
            sys.stdout.write("#")
        i = i + 1
    else:
        print(lable + "\n")

for item in series_filter_set:
    f_carseriesname_count_filter.write(item + "\n")

f.close()
outf_train.close()
outf_test.close()
f_carseriesname_count_filter.close()
print("\nWord segmentation complete.")
print(i)
