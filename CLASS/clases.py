# Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
    #          - show_full_name
    #          - year_of_birth
    #          - show_initials

class Student:
    first_name="Ann"
    second_name="Anyango"
    age=20
    country="Kenya"

def __init__(self,show_full_name,year_of_birth,show_initials):
    self.show_full_name=show_full_name
    self.year_of_birth=year_of_birth
    self.show_initials=show_initials
student=Student()   
print (f"Student:,{student.first_name} {student.second_name}") 
print (f"Student:,{student.first_name[0]} {student.second_name[0]}")
print(f"Student:,{20} years old,   year of birth{2003}")


#  Create 3 files in the classes directory car.py, fruit.py, 
# and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.


   