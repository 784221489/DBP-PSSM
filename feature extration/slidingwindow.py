import numpy as np
import pandas as pd
window = 3
ws = 5
np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# 定义路径
def readfile(strpath):
    with open(strpath) as f:
        line = f.read()
        line = line.split('\n')
        line1 = line[3:]
        line = []
        for i in range(len(line1)):
            if len(line1[i]) == 0:
                break
            line.append(line1[i])
        line1 = line
        line = []
        for i in range(len(line1)):
            line1[i] = line1[i].split(" ")
            line1[i] = [x for x in line1[i] if x != '']
            line.append(line1[i][2:22])
        line = np.array(line).astype(np.float)
    return line


    
def slidingwindow(line):
    zero = np.zeros((1, 20))
    line1 = np.concatenate((zero, line, zero))
    a = []
    b = []
    for i in line1:
        a.append(i)
    n = len(line1) - window + 1
    for i in range(n):
        b.append(np.concatenate((a[i], a[i + 1], a[i + 2]), axis=0))
    df = pd.DataFrame(b)
    m = len(df)
    for i in range(m - ws + 1):
        for j in range(ws):
            if i + j != i:
                df.iloc[i] += df.iloc[i + j]
    for i in range(m - ws + 1, m):
        df.drop([i], inplace=True)

    feature = []
    feature.extend(df.mean())
    feature.extend(df.std())
    feature.extend((df.max()-df.min()))
    feature.extend(df.quantile(0.25))
    feature.extend(df.quantile(0.75))
    return feature



def transtofeature(countpositive,countnegative):
    featurepositive=[]
    for i in range(countpositive):
        print(i)
        (line)=readfile('E:/Graduate/DNA-Binding/data/rank-pssm/newDNArset-positive/'+str(i)+'.pssm')
        feature = slidingwindow(line)
        featurepositive.append(feature)
    featurenegative=[]
    for i in range(countnegative):
        print(i)
        line=readfile('E:/Graduate/DNA-Binding/data/rank-pssm/newDNArset-negative/'+str(i)+'.pssm')
        feature = slidingwindow(line)
        featurenegative.append(feature)
    labelnegative=np.zeros(countnegative,dtype='int')
    labelpositive=np.ones(countpositive,dtype='int')
    feature=[]
    feature.extend(featurepositive)
    feature.extend(featurenegative)
    np.savetxt('C:/Users/cpc/Desktop/slidingwindow.csv', feature, delimiter=',')
    label=[]
    label.extend(labelpositive)
    label.extend(labelnegative)
    np.savetxt('C:/Users/cpc/Desktop/label.csv', label, delimiter=',')
#transtofeature()
import sys
print("jiaobenmin", sys.argv[0])
countpositive=int(sys.argv[1])
countnege=int(sys.argv[2])
transtofeature(countpositive,countnege)





    
  