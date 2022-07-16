a=list(map(int,input().split()))
b=int(input())
m=0
for i in a:
    if b==i:
        m+=1
print(m)
