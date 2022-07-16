a=list(map(int,input().split()))
b=int(input())
c=-1

for i in a:
    if i==b:
        c+=1
        print(c,end=' ')
    else:
        c+=1
