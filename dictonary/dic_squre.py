##a={}
##for i in range(1,6):
##    a[i]=i*i
##
##print(a)


##a={i:i*i for i in range(1,6)}
##print(a)

a=[1,2,3,1,2,4]
d={}

for i in a:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1

print(d)
        
