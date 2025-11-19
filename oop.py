class Employee:

    raise_amount = 1.20

    #Constructor
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@gmail.com'

    #class Method
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise_by_10_percent(self):
        self.pay = int(self.pay * 1.10)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

#instance variables
"""
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.name = "Satya"
emp_1.last = "Trivedi"
emp_1.email = "satya@123"
emp_1.pay = 10000

emp_2.name = "Satya"
emp_2.last = "Trivedi"
emp_2.email = "satya@123"
emp_2.pay = 10000

print(emp_1.email)
print(emp_2.email)
"""

#instance using constructor
emp_2 = Employee('satya','trivedi',20000)
print(emp_2.email)
"""
    if we create parameterised constrictor, Python will not create any default constructor
    Python can have at most ONE __init__ method per class. 
"""

print('{} {}'. format(emp_2.first_name, emp_2.last_name) )
print(emp_2.full_name())

#we cal also run class methods using class name
print(Employee.full_name(emp_2))

"""
    using class variable 
    can access the class variable from both class and its instance variable
"""

emp_2.apply_raise_by_10_percent()
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)
print(Employee.raise_amount)