a=list(map(int,input().split()))
b=int(input())

for i in range (len(a)):
    if a[i]==b:
        print(a.index(b))
        a[i]=-5
