a=list(map(int,input().split()))

for i in a:
    '''if a.count(i)>1:
        print(i,end=' ')'''
    if i not in b and a.count(i)>1:
        b.append(i)
print(*b)
        
    
