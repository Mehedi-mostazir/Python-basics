from dis import COMPILER_FLAG_NAMES


class student():
    college='ACOE'
    def __init__(self,name,roll,college,m1,m2):
        self.name=name
        self.roll=roll
        self.college=college 
        self.m1=m1
        self.m2=m2
        self.avg=(m1+m2)/2
    def display(self):
        print(self.name,self.roll,self.college,self.avg)

a=student('mehedi','05b3','ACOE',100,60)
a.display()

#c=student('md mostazir','21mh',)
#c.display()