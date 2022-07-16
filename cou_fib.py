def fib(n):
    a,b=0,1
    count=3
    #print(a,b,end=' ')
    while True:
        c=a+b
        #print(c,end=' ')
        a=b
        b=c
        if c==n:
            print(count)
            break
        elif n==1:
            print('1')
            break
        elif n==0:
            print('0')
            break
        count +=1
            
            
    
n=int(input())
fib(n)
