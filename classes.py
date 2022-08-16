class emp:
    def __init__ (self,name,sal,city='Newyork'):
        self.name = name
        self.sal = sal
        self.city = city

    def display(self):
        print(self.name,self.sal,self.city,sep=' - ')


x1 = emp('samyak',45000,'LA')
x2 = emp('krishna',100000)

x2.display()
x1.display()


