##n=input()
##
##b=0
##
##for i in n:
##    if i in '0123456789':
##        b+=1
##
##print(b)


##n=input()
##c=0
##for i in n:
##    if ord(i)>=48 and ord(i)<=57:
##        c+=1
##
##print(c)


##a=input()
##c=[]
##d=[]
##
##for i in range(len(a)):
##    if i%2 ==0:
##        c.append(a[i])
##    if i%2 !=0:
##        d.append(a[i])
##e=''.join(c)
##f=''.join(d)
##print(e+f)



##a=input()
##s1=''
##s2=''
##for i in range(0,len(a)):
##    if i%2==0:
##        s1+=a[i]
##    else:
##        s2+=a[i]
##print(s1+s2)


a=input()
print(a[::2]+a[1::2])
    








