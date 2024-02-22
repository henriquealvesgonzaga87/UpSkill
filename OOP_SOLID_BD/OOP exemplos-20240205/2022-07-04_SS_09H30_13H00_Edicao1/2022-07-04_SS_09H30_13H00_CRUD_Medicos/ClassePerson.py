# https://www.tutorialspoint.com/python/python_classes_objects.htm

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


# ----
class Person:

    def __init__(self, name, age, salary):
        self.name   = name
        self.age    = age
        self.salary = salary

    def get_first_name(self):
        return self.name.split()[0]

    def get_last_name(self):
        return self.name.split()[1]

    def update_salary(self, new_salary):
        self.salary = new_salary

    def compute_salary_after_tax(self, irs=0.32, ss=0.15):
        return self.salary - (self.salary * irs) - (self.salary * ss)

person1 = Person("João Silva", 35, 1500)
person2 = Person("Ana Costa", 27, 2000)

print(person1.get_last_name())
print(person2.get_last_name())


class Manager(Person): # Define a subclass of Person
    def compute_salary_after_tax(self, irs=0.45, ss=0.25):
        return Person.compute_salary_after_tax(self, irs, ss) + (self.salary * 0.10)

class Developer(Person):
    def compute_salary_after_tax(self, irs=0.35, ss=0.17):
        return Person.compute_salary_after_tax(self, irs, ss)

manager1 = Manager("Rui Oliveria", 78, 5000)
print(manager1.compute_salary_after_tax())

manager2 = Developer("Inês Leão", 78, 2750)
print(manager2.compute_salary_after_tax())
