import os
import numpy as np
import pandas as pd
import re

path = "E:\\Graduate\\DNA-Binding\\data\\original data\\newDNArset.fasta"
proteinname = []
seq = []
length = []
with open(path) as content:
    lines = content.readlines()
    for i in lines:
        if i[0] == ">":
            proteinname.append(i[1:7])
        else:
            seq.append(i)
            length.append(len(i) - 1)
acid = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
df = pd.DataFrame(columns=acid, index=proteinname)
df = df.fillna(0)

protein = dict(zip(proteinname, seq))
for i in protein.keys():
    j = protein[i]
    for k in acid:
        count = j.count(k)
        df.loc[i, k] = count
df['length'] = length
for i in acid:
    df[i] = df[i] / df['length']

df.to_csv('E:\\Graduate\\DNA-Binding\\data\\feature\\newDNArset\\频率.csv', sep=',', header=True)


