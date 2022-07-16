
def rev(n):
    res=0
    while(n>0):
        rem=n%10
        res=res*10+rem
        n=n//10
    return res

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 1
            break
    else:
        return 0


x=int(input())
temp=x
if x==1:
    y=rev(temp)
    z=prime(y)
    if z==1:
        print("given number is twisted prime")
    else:
        print("given number is not twisted prime")
else:
    print("given number is not prime")        
