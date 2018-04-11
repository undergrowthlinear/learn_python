import numpy as np
import pandas as pd

print('pd version:', pd.__version__)
'''
pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
'''
# 列表
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
# 字典
# pd.DataFrame({'City name': city_names, 'Population': population})
# 读csv文件
california_housing_dataframe = pd.read_csv("../california_housing_train.csv",
                                           sep=",")
print(california_housing_dataframe.describe())
# 看头文件
print(california_housing_dataframe.head())


california_housing_dataframe.hist('housing_median_age')

cities = pd.DataFrame({'City name': city_names, 'Population': population})
print(type(cities['City name']))
# cities['City name']

print(type(cities['City name'][1]))
# cities['City name'][1]

print(type(cities[0:1]))
#cities[0:2]

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities[
    'Area square miles']
print(cities)

cities['is San'] = (cities['City name'].apply(
    lambda name: name.startswith('San'))) & (cities['Area square miles'] > 50)
print(cities)

print(city_names.index,cities.index)
print(cities.reindex([2, 0, 1]))

print(cities.reindex(np.random.permutation(cities.index)))

print(cities.reindex([3, 2, 0, 1]))

'''
population / 1000

np.log(population)

population.apply(lambda val: val > 1000000)

'''
