import csv
import math

# Step 1: Read CSV Data
def load(filename):
    data = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header row
        for line in file:
            row = line.strip().split(',')
            features = row[1:-1]  # Age, income, student, credit_rating
            label = row[-1]       # buys_computer
            data.append((features, label))
    return data

def entropy(data):
    ent=0
    clas={}
    for feature,label in data:
        if label not in data:
            clas[label]=0
        clas[label]+=1
    for label in clas:
        p=clas[label]/len(data)
        ent-=p*math.log2(p)
    return ent

def splitdata(index,value,data):
    trueb=[row for row in data if row[0][index]==value]
    falseb=[row for row in data if row[0][index]!=value]
    return trueb,falseb

def bestsplit(data):
    bestgain=0
    bestindex=None
    bestvalue=None
    ent=entropy(data)
    n=len(data[0][0])
    for i in range(n):
        values=set(row[0][i]for row in data)
        for value in values:
            true,false=splitdata(i,value,data)
            if not true or not false:
                continue
            p=len(true)/n
            gain=ent-p*entropy(true)-(1-p)*entropy(false)
            if gain>bestgain:
                bestgain,bestindex,bestvalue=gain,i,value
    return bestgain,bestindex,bestvalue

class Decision:
    def __init__(self,index=None,value=None,true=None,false=None,prediction=None):
        self.index = index
        self.value = value
        self.true = true
        self.false = false
        self.prediction = prediction
def buildtree(data):
    gain,index,value=bestsplit(data)
    if gain==0:
        return Decision(prediction=data[0][1])
    true,false=splitdata(index,value,data)
    truenode=buildtree(true)
    falsenode=buildtree(false)
    return Decision(index=index, value=value, true=truenode, false=truenode)

def printtree(node,headers,spacing=''):
    if node.prediction is not None:
        print(spacing+f'predict : {node.prediction}')
        return
    print(f'{spacing} {headers[node.index]}=={[node.value]}??')
    print(spacing+'-->true')
    printtree(node.true,headers,spacing='')
    print(spacing+'-->false')
    printtree(node.false,headers,spacing='')


filen='dec.csv'
trans=load(filen)
headers = ['age', 'income', 'student', 'credit_rating']  # Feature names
tree=buildtree(trans)
printtree(tree,headers)
