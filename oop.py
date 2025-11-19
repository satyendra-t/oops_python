class Employee:
    pass

#instance variables
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