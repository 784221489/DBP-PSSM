import os
from sklearn.metrics import roc_auc_score, roc_curve
import numpy as np
import pandas as pd
import re


def gety_scores(filepath):
    result = []
    with open(filepath) as content:
        lines = content.readlines()
        for i in lines:
            res = list(
                filter(None, i.split(" ")))  # 此处必须加一个list，因为filter转化后要以list展示，否则报错error<filter object at 0x02C18A70>
            result.append(res)
    del (result[0])
    for i in result:
        del (i[-1])
        del (i[0])
    y_scores = np.array(result).astype(np.float)
    return y_scores


y1 = pd.read_csv(
    "E:\\Graduate\\DNA-Binding\\data\\feature_selection\\pdb1075\\no frequency\\144select_feature\\min-max\\fold1.csv")
y2 = pd.read_csv(
    "E:\\Graduate\\DNA-Binding\\data\\feature_selection\\pdb1075\\no frequency\\144select_feature\\min-max\\fold2.csv")
y3 = pd.read_csv(
    "E:\\Graduate\\DNA-Binding\\data\\feature_selection\\pdb1075\\no frequency\\144select_feature\\min-max\\fold3.csv")
y4 = pd.read_csv(
    "E:\\Graduate\\DNA-Binding\\data\\feature_selection\\pdb1075\\no frequency\\144select_feature\\min-max\\fold4.csv")
y5 = pd.read_csv(
    "E:\\Graduate\\DNA-Binding\\data\\feature_selection\\pdb1075\\no frequency\\144select_feature\\min-max\\fold5.csv")
y1_true = y1.iloc[:, 0].values
y2_true = y2.iloc[:, 0].values
y3_true = y3.iloc[:, 0].values
y4_true = y4.iloc[:, 0].values
y5_true = y5.iloc[:, 0].values
y_true = []
y_true.append(y1_true)
y_true.append(y2_true)
y_true.append(y3_true)
y_true.append(y4_true)
y_true.append(y5_true)

auc = []
name = []
# 主路径
path = "E:\\TDDOWNLOAD\\allfeaturez-score"
pathlist1 = os.listdir(path)
pathlist2 = []
for i in pathlist1:
    pathlist2.append(path + "\\" + i)
##文件名列表
filelist = os.listdir(pathlist2[1])
filepath = []
filename = []
for i in filelist:
    if i[-3:] == 'out':
        filename.append(i)
for i in pathlist2:
    for j in filename:
        f = i + '\\' + j
        y_scores = gety_scores(f)
        for k in y_true:
            if all(k == y1_true) and j[2] == str(1):
                auc1 = roc_auc_score(k, y_scores)
            elif all(k == y2_true) and j[2] == str(2):
                auc2 = roc_auc_score(k, y_scores)
            elif all(k == y3_true) and j[2] == str(3):
                auc3 = roc_auc_score(k, y_scores)
            elif all(k == y4_true) and j[2] == str(4):
                auc4 = roc_auc_score(k, y_scores)
            elif all(k == y5_true) and j[2] == str(5):
                auc5 = roc_auc_score(k, y_scores)
    aucaverage = auc1 + auc2 + auc3 + auc4 + auc5
    auc.append(aucaverage / 5)
    name.append(i)
auc = pd.DataFrame(data=auc)
auc['name'] = pd.DataFrame(data=name)

auc.to_csv('E:\\TDDOWNLOAD\\allz-scoreauc.csv', sep=',', header=True)










