class car():
    country='india'  #class variable
    def __init__(self,name,model):  #constractor
        #instance variables
        self.name=name
        self.model=model
    def display(self):  #function
        print(self.name,self.model,self.country)


a=car('kia',1234)  #calling oject is enough
a.display() #we have to call function

c=car('Maruti',5678)
c.display()