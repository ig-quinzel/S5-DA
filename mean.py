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
  
