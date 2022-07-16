a=list(map(int,input().Split()))
b=int(input())

##print(a.index(b))
for i in range (len(a)):
    if a[i]==b:
        print(i,end=' ')
