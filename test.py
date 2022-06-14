from random import randint #ブースト勧誘
lis=[]
count=0
trial=300
while count<trial:
  b=True
  x=50 #確率
  y=0
  z=0 #回数
  while True:
    y=0
    a=False
    while y<11:
      A=randint(1,33)
      B=randint(1,100)
      if A==1 and B<x:
          a=True
      y+=1
    x+=5
    z+=11
    if a==True:
      #print(z)
      break
  lis.append(z)
  count+=1
print(sum(lis)/trial)