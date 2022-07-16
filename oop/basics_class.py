

class car():
    def __init__(self,name,model):   #constractor
        self.name=name
        self.model=model
        
    def display(self):
        print(self.name,self.model)

a=car('kia',1234)
a.display()

c=car("tata",5678)
c.display()
