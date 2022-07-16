def bindec(n):
    i=0
    r=0
    while n:
        rem=n%10
        r=r+rem*(2**i)
        n//=10
        i+=1
    return r

print("enter bin val:")
n=int(input())
print(bindec(n))
        
        
