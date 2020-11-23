import numpy as np
import pandas as pd

np.set_printoptions(threshold=np.inf)


# 定义路径
def readfile(strpath):
    with open(strpath) as f:
        line = f.read()
        line = line.split('\n')
        line1 = line[3:]
        line = []
        hangindex = []
        for i in range(len(line1)):
            if len(line1[i]) == 0:
                break
            line.append(line1[i])
        line1 = line
        line = []
        for i in range(len(line1)):
            hangindex.append(line1[i][6])
        for i in range(len(line1)):
            line1[i] = line1[i].split(" ")
            line1[i] = [x for x in line1[i] if x != '']
            line.append(line1[i][2:22])
        line = np.array(line).astype(np.float)
    return line, hangindex


def standard(line, hangindex):
    max_col = np.max(line, axis=0)
    min_col = np.min(line, axis=0)
    fstandard = np.empty(line.shape)
    for i in range(len(line)):
        for j in range(len(line[0])):
            fstandard[i][j] = (line[i][j] - min_col[j]) * 1.0 / (max_col[j] - min_col[j])
    df = pd.DataFrame(data=fstandard, index=hangindex,
                    columns=['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W',
                            'Y', 'V'])

    return df

def add(b):
    c = 0
    for i in b:
        c += i
    return c

def pssm400(df):
    acid = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    feature = {}
    for i in acid:
        for j in acid:
            feature[i + j] = 0
    col = df.columns.tolist()
    hang = df.index.tolist()
    feakey = feature.keys()

    for i in feakey:
        for j in col:
            for k in hang:
                if j + k == i:
                    b = df.at[k, j].tolist()
                    if type(b) == float:
                        feature[i] = b
                    elif type(b) == list:
                        c = add(b)
                        feature[i] = c


                    break


    return list(feature.values())
def transtofeature(countpositive,countnegative):
    featurepositive=[]
    for i in range(countpositive):
        print(i)
        (line,hangindex)=readfile('E:/Graduate/DNA-Binding/data/rank-pssm/newDNArset-positive/'+str(i)+'.pssm')
        df = standard(line, hangindex)
        feature=pssm400(df)
        featurepositive.append(feature)
    featurenegative=[]
    for i in range(countnegative):
        print(i)
        (line,hangindex)=readfile('E:/Graduate/DNA-Binding/data/rank-pssm/newDNArset-negative/'+str(i)+'.pssm')
        df = standard(line, hangindex)
        feature=pssm400(df)
        featurenegative.append(feature)
    labelnegative=np.zeros(countnegative,dtype='int')
    labelpositive=np.ones(countpositive,dtype='int')
    feature=[]
    feature.extend(featurepositive)
    feature.extend(featurenegative)
    np.savetxt('C:/Users/cpc/Desktop/feature.csv', feature, delimiter=',')
    label=[]
    label.extend(labelpositive)
    label.extend(labelnegative)
    np.savetxt('C:/Users/cpc/Desktop/label.csv', label, delimiter=',')










import sys
print("jiaobenmin", sys.argv[0])
countpositive=int(sys.argv[1])
countnegative=int(sys.argv[2])

transtofeature(countpositive,countnegative)







