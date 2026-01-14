class Employee:
    start_Time="10am"
    end_Time="5pm"
    
class adminstaff(Employee):
    def __init__(self,role):
        self.role=role
        
class account(adminstaff):
    def __init__(self, salary,role):
        super().__init__(role)
        self.salary=salary
        

acc=account(25000,"CA")
print(acc.salary,acc.role,acc.end_Time)


Inheritance Concept

        

