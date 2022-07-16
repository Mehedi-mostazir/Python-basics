n=int(input())
a=list(map(int,input().split()))

for i in range (n):
    c=0
    if a.count(a[i])==1:
        print(a[i],end='')
