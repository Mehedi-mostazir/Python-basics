n=int(input())
for i in range(2,(n//2)+1):
    if n%i==0:
      print('Not prime')
      break
else:
    d=0
    pd=0
    while n:
        n=n//10
        r=n%10
        d+=1
        for i in range(2,(r//2)+1):
            if n%i==0:
                break
        else:
            pd+=1
    if d==pd:
        print('Mega prime')
    else:
        print('Not mega prime')            
