"""
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

s1.info()  # equivalent to student.info(s1)
s2.info()

#a function is something which can be called independently but method needs to be called by class
# hence they're dependent to be called upon.

#no matters what name you passed it will act as a self
class office:
    def __init__(c,i):
        c.i = i
    
    def info(i):
        print(i.i)

o1 = office(1)
o1.info()

"""

#if the value of the object varies from object to object is
#called instance variable

class Student:
    c = 10
    def __init__(self,name,rollno):
        "__docstring__ constructor"
        self.name = name
        self.rollno = rollno

    def info(self):
        self.marks = 70
        x=10

s1 = Student('samyak',101)
#before calling the info we have only2 instance variable are there

print(s1.__dict__)
s1.info()

#after info method 1 is added. 
print(s1.__dict__)
#using the __dict__ we can get all the instance variables details
#using __dict only instance variable are shown
#x=10, c=10 is not shown
s1.tell = 10 
print(s1.__dict__)


