import numpy as np
import math
n=int(input("length"))
data=[]
for i in range(n):
    num=int(input(f'enter num{i+1}'))
    data.append(num)
sum=0
for i in range(n):
    sum+=data[i]
mean=sum/n
print(f'mean:{mean}')
data.sort()
if n%2==1:
    median=data[(n)//2]
else:
    median=(data[(n//2)]+data[(n//2)-1])/2
print(f'median: {median}')
lend={}
for i in data:
    if i in lend:
      lend[i]+=1
    else:
      lend[i]=1
maxx=max(lend.values())
mode=[k for k,v in lend.items() if v==maxx]
print(f'mode:{mode}')
if len(mode)==1:
    print("unimode")
elif len(mode)==2:
     print("bimode")
else:
    print("trimode")
q1=data[int(len(data)*0.25)]
q2=median
q3=data[int(len(data)*0.75)]
iqr=q3-q1
lo=q1-(1.5*iqr)
ho=q3+(1.5*iqr)
print(q1,q2,q3)
print(lo,ho)
new=[]
for i in data:
    if i>lo and i<ho:
        new.append(i)
print(new)
print("max",max(new))
print("min",min(new))
vari=np.var(new)
sd=math.sqrt(vari)
print("variane:",vari,"sd:",sd)




