n=input()
temp=int(n)
temp2=temp
L=len(n)
L2=L
c=0
for i in range(2,int(temp**0.5)+1):
    if temp%i==0:
        while(L>0):
            r=temp2%10
            for j in range(2,int(r**0.5)+1):
                c+=1


if c==L2:
     print("megaprime")          
else:
    print("not megaprime")

  