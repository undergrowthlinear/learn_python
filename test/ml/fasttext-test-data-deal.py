# coding :utf8
#author linxinzhu from https://blog.csdn.net/Season_For_Lin/article/details/78568991
import jieba
import sys
i = 0
count=0
f = open("E:\\java_other\\python\data\\fasttext_test\\series_rela"
         "\\tmp_dwd_base_article_carseriesname-test-origin.txt", 'r',encoding='utf8')
outf = open("E:\\java_other\\python\data\\fasttext_test\\series_rela"
            "\\tmp_dwd_base_article_carseriesname-test.txt",'w',encoding='utf8')

for line in f:
    line=line.strip()
    l_ar=line.split("\001")
    if len(l_ar)!=4:
        continue
    id=l_ar[0]
    title=l_ar[2]
    content=l_ar[3]
    lable=l_ar[1]
    l_lable=lable.split(",")
    lable=l_lable[0]
    seg_title=jieba.cut(title.replace("\t"," ").replace("\n"," "))
    seg_content=jieba.cut(content.replace("\t"," ").replace("\n"," "))
    outline = " ".join(seg_title)+" "+" ".join(seg_content)
    outline = outline+"\n"
    outf.write(outline)

    if i%2500 == 0:
        count=count+1
        sys.stdout.flush()
        sys.stdout.write("#")
    i=i+1

f.close()
outf.close()
print("\nWord segmentation complete.")
print(i)