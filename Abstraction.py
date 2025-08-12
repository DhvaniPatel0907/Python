from abc import ABC,abstractmethod

class Employer(ABC):
    def salary(self):
        pass

class Krutarth(Employer):
    def salary(self):
        return 10000
    
class Dhvani(Employer):
    def  salary(self):
        return 12000
    
obj = Krutarth()
print("Krutarth's Salary is")
print(obj.salary())

obj1=Dhvani()
print("Dhvani's Salary is")
print(obj1.salary())