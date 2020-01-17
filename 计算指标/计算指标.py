# 测试集计算指标
import pandas as pd
import numpy as np

path = "E:\\python3\\Lib\\site-packages\\libsvm-3.23\\windows\\pssm400.train.model.out"
result = []
acc = []
tpp = []
tnn = []
fpp = []
fnn = []
with open(path) as content:
    lines = content.readlines()
    for i in lines:
        res = list(filter(None, i.split(" ")))  # 此处必须加一个list，因为filter转化后要以list展示，否则报错error<filter object at 0x02C18A70>
        result.append(res)
del (result[0])
a = []
score = []
for i in result:
    del (i[-1])
    del (i[0])
    a.extend(i)
for i in a:
    j = float(i)
    score.append(j)
threshold = []
for i in range(1, 101):
    threshold.append(i * 0.01)

for i in threshold:
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for j in score:
        k = score.index(j)
        if j >= i and k <= 92:
            tp += 1
        if j < i and k <= 92:
            fn += 1
        if j >= i and k > 92:
            fp += 1
        if j < i and k > 92:
            tn += 1
    tpp.append(tp)
    tnn.append(tn)
    fpp.append(fp)
    fnn.append(fn)
    acc.append((tp + tn) / len(score))
acc = pd.DataFrame(data=acc)
acc['threshold'] = threshold
acc['tp'] = tpp
acc['tn'] = tnn
acc['fp'] = fpp
acc['fn'] = fnn
acc['sn'] = acc['tp'] / (acc['tp'] + acc['fn'])
acc['sp'] = acc['tn'] / (acc['tn'] + acc['fp'])
acc['mcc'] = (acc['tn'] * acc['tp'] - acc['fp'] * acc['fn']) / np.sqrt(
    (acc['tn'] + acc['fp']) * (acc['tn'] + acc['fn']) * (acc['tp'] + acc['fn']) * (acc['tp'] + acc['fp']))
acc.to_csv('E:\\TDDOWNLOAD\\pssm400指标.csv', sep=',', header=True)







