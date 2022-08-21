class emp:
    '''doc string (This is a employee class)'''
    def __init__(self):
        print("this is self ",id(self))
        '''this is __init__'''
        pass
    '''overwriting the doc string '''

print(emp.__doc__)
print(emp.__init__.__doc__)
print(emp.__doc__) # it seems that FCFS is followed only the first line is treated as doc else comments

e1 = emp()
print("this is e1- ",id(e1))

class student:
    '''This is a student class'''
    def __init__(self,name,add):
        self.name = name
        self.add = add
    def info(self):
        print("Name is = ",self.name)
        print("Address is - ",self.add)
        print("__"*20)


s1 = student("samyak","bharat")
s2 = student("krishna","mathura")

s1.info()
s2.info()