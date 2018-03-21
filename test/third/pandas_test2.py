import csv

import pandas as pd
import numpy as np

m_file = '../marks.csv'
#
with open(m_file) as f:
    for l in f:
        print(l)

#
dir(csv)

csv_reader = csv.reader(open(m_file))
for l in csv_reader:
    print(l)

#
marks = pd.read_csv(m_file)
print(marks['english'])
print(marks)
print(marks.reindex(np.random.permutation(marks.index)))
