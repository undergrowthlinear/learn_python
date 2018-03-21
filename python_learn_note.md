# 参考
- https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/1-2-install/
# 学习
- 学习路线
    - python基础----python常用numpy/pandas/scikit----ml----tensorflow 
- need know

```
解释型的语言 跨平台 从规范到解释器都是开源的
CPython是使用最广的Python解释器 用>>>作为提示符
IPython是基于CPython之上的一个交互式解释器 用In [序号]:作为提示符
Python程序是大小写敏感
变量本身类型不固定的语言称之为动态语言
```
- Python从入门到实践
```
python python3 <<<
geany exit() sublime traceback
小写变量名 字符串 title upper lower
+ \t \n rstrip lstrip strip print
+-*/** str # import this python之蝉
- 列表 [,,] [0] [-1] [0:3] [:] append insert del pop remove sort sorted reverse len 
- 元组 () 
for ... in list: 缩进 range list
min max sum 列表解析 
== ！= and or in not in 
if / if else ／ if elif else
- 字典 键值对 顺序不同 {} 类比json
del stu['name'] items keys values
set 嵌套 列表中字典 字典中字典 字典中列表
input int while break  continue 循环列表 
def 函数 形参 实参 位置实参 关键字实参 return 可变形参与元组(*)与字典(**)
import from module_name import fun
as alias 
- class Dog(): def __init__(self) 
super  驼峰 小写
- 文件与异常 with open(dir,rwar+) as fp
read readlines write try-except-else  pass 
json.dump json.load 
unittest.TestCase  test开头 
unittest.main assertEqual setUp 
- 数据可视化 matplotlib pyplot plot show scatter savefig  pygal.Bar  
- csv enumerate datetime strptime
json  None 
- requests 
- web应用-Django 
```
- Python机器学习实践指南
```
https://github.com/packtpublishing/
pythonmachinelearningblueprints
获取--requests
检查、探索--jupyter pandas df.ix matplotlib numpy seaborn map apply groupby arraymap 
清理、准备
建模--statsmodels scikit-learn 
评估
部署
```
## pandas
- pandas 是一种列存数据分析 API
    - DataFrame，您可以将它想象成一个关系型数据表格，其中包含多个行和已命名的列
    - Series，它是单一列。DataFrame 中包含一个或多个 Series，每个 Series 均有一个名称。
## Code
- ml learn

```
import pandas as pd
import numpy as np
pd.__version__

pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })

california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/ml_universities/california_housing_train.csv", sep=",")
california_housing_dataframe.describe()

california_housing_dataframe.head()

# california_housing_dataframe.hist('housing_median_age')

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
cities['City name']

print(type(cities['City name'][1]))
cities['City name'][1]

print(type(cities[0:1]))
cities[0:2]

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
cities

cities['is San'] = (cities['City name'].apply(lambda name:name.startswith('San'))) & (cities['Area square miles'] > 50)
cities

city_names.index
cities.index
cities.reindex([2, 0, 1])

cities.reindex(np.random.permutation(cities.index))

cities.reindex([3,2, 0, 1])

'''
population / 1000

np.log(population)

population.apply(lambda val: val > 1000000)

'''


```
