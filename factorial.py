

#normal methode

#def sample(n):
#   r=1
#    for i in range(1,n+1):
#        r*=i
#   return r
#n=int(input())
#print(sample(n))



#using recursion
def sample(n):
    if n==1:
        return 1
    return n* sample(n-1)
n=int(input())
print(sample(n))

