import pandas as pd
import numpy as np

df=pd.read_csv('input.csv')
print(df)
a=list(df['a'])
b=list(df['b'])
meana=np.mean(a)
meanb=np.mean(b)
l=len(a)
cornum=0
cordem=0
for i in range(l):
    cornum+=(a[i]-meana)*(b[i]-meanb)
    cordem+=np.sqrt(((a[i]-meana)**2)*((b[i]-meanb)**2))
cor=cornum/cordem
print("correlation coefficient : ",cor)
if cor>0:
    print("positive correlation")
elif cor<0:
    print("negative correlation")
else:
    print("no correlation")
cov=cornum/l
print("covariance : ",cov)
