import random
import pandas as pd

from random import shuffle
random.seed(2)
num = list(range(1075))
shuffle(num)


df = pd.read_csv("E:\Graduate\DNA-Binding\data\\feature_selection\\feature\\pdb1075\\min-max.csv",low_memory=False)

data1 = pd.DataFrame()
data2 = pd.DataFrame()
data3 = pd.DataFrame()
data4 = pd.DataFrame()
data5 = pd.DataFrame()
for i in df.index.tolist():
    if i in num[:215]:
        data1 = data1.append(df.iloc[i,:])
for i in df.index.tolist():
    if i in num[215:430]:
        data2 = data2.append(df.iloc[i,:])
for i in df.index.tolist():
    if i in num[430:645]:
        data3 = data3.append(df.iloc[i,:])
for i in df.index.tolist():
    if i in num[645:860]:
        data4 = data4.append(df.iloc[i,:])
for i in df.index.tolist():
    if i in num[860:]:
        data5 = data5.append(df.iloc[i,:])
data1.to_csv('E:\\Graduate\\DNA-Binding\\data\\feature_selection\\feature\\pdb1075\\fold1.csv',sep = ',',header=True)
data2.to_csv('E:\\Graduate\\DNA-Binding\\data\\feature_selection\\feature\\pdb1075\\fold2.csv',sep = ',',header=True)
data3.to_csv('E:\\Graduate\\DNA-Binding\\data\\feature_selection\\feature\\pdb1075\\fold3.csv',sep = ',',header=True)
data4.to_csv('E:\\Graduate\\DNA-Binding\\data\\feature_selection\\feature\\pdb1075\\fold4.csv',sep = ',',header=True)
data5.to_csv('E:\\Graduate\\DNA-Binding\\data\\feature_selection\\feature\\pdb1075\\fold5.csv',sep = ',',header=True)
