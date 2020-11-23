import numpy as np

def readfile(strpath):
    f=open(strpath)
    line=f.read()
    line=line.split('\n')
    line1 = line[3:]
    line = []
    for i in range(len(line1)):
        if len(line1[i]) == 0:
            break
        line.append(line1[i])
    line1 = line
    line = []
    for i in range(len(line1)):
        line1[i]=line1[i].split(" ")
        line1[i]=[x for x in line1[i] if x != '']
        line.append(line1[i][2:22])
# print line
    line=np.array(line).astype(np.float)
    return line
def local_DPP_1221gai(line,n1,lamudamax1):
    avg=np.mean(line,axis=1)
    var=np.var(line,axis=1)
    var=np.sqrt(var)
    f=np.empty(line.shape)
    for i in range(len(line)):
        for j in range (len(line[0])):
            if var[i]==0:
                f[i][j]=0
            else:
                #print('di'+str(i)+'hang,di'+str(j)+'lie:avg'+str(avg[i])+'biaozhuncha:'+str(var[i]))
                f[i][j]=(line[i][j]-avg[i])*1.0/var[i]
    p=[]
    n=n1
    p.append(f[:(len(f)//3)])
    p.append(f[(len(f)//3):(2*len(f)//3)])
    p.append(f[(2*len(f)//3):])
    feature=[]
    lamudamax=lamudamax1+1
    avgcol=np.mean(line,axis=0)
    for k in range(len(p)):
        for j in range(20):
            sum=0
            for i in range(len(p[k])):
                    sum=sum+p[k][i][j]
            if(len(p[k]) !=0):
                sum=sum*1.0/(len(p[k]))
            feature.append(sum)
        for j in range(20):
            sum=0
            lamuda=1
            while lamuda<lamudamax:
                for i in range(len(p[k])-lamuda):
                        sum=pow((p[k][i][j])-(p[k][i+lamuda][j]),2)+sum
                if((len(p[k])-lamuda)!=0):
                    sum=sum*1.0/(len(p[k])-lamuda)  
                feature.append(sum)
                lamuda=lamuda+1
    #print len(feature)
    return feature
def transtofeature(countpositive,countnege,lamudamax,n):
    featurepositive=[]
    for i in range(countpositive):
        print(i)
        line=readfile('E:/Graduate/DNA-Binding/data/rank-pssm/pdb186-positive/'+str(i)+'.pssm')
        feature=local_DPP_1221gai(line,n,lamudamax)
        featurepositive.append(feature)
    featurenegative=[]
    for i in range(countnege):
        print(i)
        linene=readfile('E:/Graduate/DNA-Binding/data/rank-pssm/pdb186-negative/'+str(i)+'.pssm')
        feature=local_DPP_1221gai(linene,n,lamudamax)
        featurenegative.append(feature)
    labelnegtive=np.zeros(countnege,dtype='int')
    labelnpositive=np.ones(countpositive,dtype='int')
    feature=[]
    feature.extend(featurepositive)
    feature.extend(featurenegative)

    np.savetxt('E:/Graduate/DNA-Binding/data/feature/'+str(n)+'a_'+str(lamudamax)+'_'+str(countnege+countpositive)+'.csv', feature, delimiter=',')
    label=[]
    label.extend(labelnpositive)
    label.extend(labelnegtive)

    np.savetxt('E:/Graduate/DNA-Binding/data/feature/'+str(n)+'b_'+str(lamudamax)+'_'+str(countnege+countpositive)+'.csv', label, delimiter=',')
#transtofeature()
import sys
print("jiaobenmin"), sys.argv[0]
countpositive=int(sys.argv[1])
countnege=int(sys.argv[2])
lamudamax=int(sys.argv[3])
n=int(sys.argv[4])
transtofeature(countpositive,countnege,lamudamax,n)