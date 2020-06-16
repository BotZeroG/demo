def display():
    print("Total Employee:")
    print(Employee.empCount)


def average():
    print("Salary Average:" )
    print(Employee.totalsal / Employee.empCount)


class Employee:
    empCount = 0
    totalsal = 0

    def __init__(self, name, salary, family, department):
        self.name = name
        self.salary = salary
        self.family = family
        self.department = department
        Employee.empCount += 1
        Employee.totalsal += salary

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary, ", Family: ", self.family, ", department: ",
              self.department)


class Fulltime(Employee):
    def __init__(self, name, salary, family, department):
        Employee.__init__(self, name, salary, family, department)

emp2 = Employee("Cara", 3000, "Zaper", "IT")

emp1 = Employee("Zara", 2000, "Caper", "IT")
emp1.displayEmployee()

display()

average()

fulltimer1 = Fulltime("Fulltime Daniel", 4000, "Hogwarts", "IT")
fulltimer1.displayEmployee()