import os
import pandas as pd
import numpy as np
import re

path = "E:\\TDDOWNLOAD\\统计\\allfeaturemin-max\\tongji_all"
Filelist = os.listdir(path)
Filepath = []
for i in Filelist:
    Filepath.append(path + "\\" + i)
accaverage = []
name = []
for i in Filepath:

    with open(i) as content:
        lines = content.readlines()
        acc = 0
        for j in lines:
            acc += float(re.findall(r'-?\d+\.?\d*e?-?\d*?', j)[0])
    accaverage.append(acc / 5)
    name.append(Filepath)

accaverage = pd.DataFrame(data = accaverage)
name = pd.DataFrame(data = name)

accaverage.to_csv('E:\\TDDOWNLOAD\\allacc.csv', sep=',', header=True)
name.to_csv('E:\\TDDOWNLOAD\\name.csv', sep=',', header=True)