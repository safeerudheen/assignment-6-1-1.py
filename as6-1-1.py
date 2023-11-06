'''
1. Part-1
Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
Each employee information consists of Name, DOB, Height, City, State. 
'''

'''
1. Part-2
Write a python program that reads this information from the JSON file and 
saves the information into a list of objects of Employee class. 
Finally print the list of the Employee objects.
'''
# 1. Part-2


import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open("employee.json", "r") as file:
    employee_data = json.load(file)

employees = []
for data in employee_data:
    employee = Employee(
        data["Name"],
        data["DOB"],
        data["Height"],
        data["City"],
        data["State"]
    )
    employees.append(employee)

for employee in employees:
    print("Name:", employee.name)
    print("DOB:", employee.dob)
    print("Height:", employee.height)
    print("City:", employee.city)
    print("State:", employee.state)
    print()
