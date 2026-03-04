
from menu import Menu

class Restaurent:
    def __init__(self,name):
        self.name=name
        #eta database er moto kaj korbe 
        self.employee_list=[]
        self.menu=Menu()

    
    def add_employee(self,employee):
        #employee add korlam employee_list e
        self.employee_list.append(employee)
    
    #sob employee ke print korlam
    def view_employee(self):
        print("----------->Employee list----------->")
        for person in self.employee_list:
            print(person.name,person.email,person.phone,person.salary,person.designation)
    
