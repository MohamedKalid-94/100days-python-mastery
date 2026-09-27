# Day 24 - Employee Management System
# Concept: Inheritance
# Goal: Practice creating a parent class and child classes that inherit from it

# --- The parent (base) class ---
class Employee:

    # --- Class attribute - shared by ALL Employee objects ---
    company_name = "TechCorp"

    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

    def show_details(self):
        print(f"{self.name} (ID: {self.employee_id}) - {self.company_name}")
        print(f"Salary: {self.get_salary()}")

    def __str__(self):
        return f"Employee: {self.name} (ID: {self.employee_id})"


# --- Child class - inherits everything from Employee ---
class Manager(Employee):

    def __init__(self, name, employee_id, base_salary, team_size):
        # super() calls the PARENT class's __init__, so we don't repeat that code
        super().__init__(name, employee_id, base_salary)
        self.team_size = team_size   # an extra attribute only Managers have

    # --- Overriding a parent method - Managers get a bonus based on team size ---
    def get_salary(self):
        bonus = self.team_size * 1000
        return self.base_salary + bonus

    # --- A method that ONLY exists on Manager, not on Employee ---
    def show_team_info(self):
        print(f"{self.name} manages a team of {self.team_size} people.")


# --- Another child class ---
class Developer(Employee):

    def __init__(self, name, employee_id, base_salary, programming_language):
        super().__init__(name, employee_id, base_salary)
        self.programming_language = programming_language

    def get_salary(self):
        # Developers get a flat skill bonus
        return self.base_salary + 5000

    def show_tech_stack(self):
        print(f"{self.name} codes in {self.programming_language}.")


# --- Creating objects of each type ---
employee1 = Employee("Ravi", "E001", 40000)
manager1 = Manager("Asha", "M001", 60000, team_size=5)
developer1 = Developer("Kalid", "D001", 50000, "Python")

# --- All of them share the base Employee behavior ---
print("--- Basic employee details ---")
employee1.show_details()
print()
manager1.show_details()   # inherited method, but get_salary() is OVERRIDDEN
print()
developer1.show_details()

# --- Each subclass still has its own EXTRA behavior ---
print("\n--- Extra behavior specific to each role ---")
manager1.show_team_info()
developer1.show_tech_stack()

# --- Checking inheritance with isinstance() and issubclass() ---
print("\n--- Type checks ---")
print("Is manager1 an Employee?", isinstance(manager1, Employee))
print("Is manager1 a Manager?", isinstance(manager1, Manager))
print("Is manager1 a Developer?", isinstance(manager1, Developer))
print("Is Manager a subclass of Employee?", issubclass(Manager, Employee))

# --- Class attributes are shared across ALL subclasses too ---
print("\n--- Shared class attribute ---")
print("employee1 company:", employee1.company_name)
print("manager1 company:", manager1.company_name)
print("developer1 company:", developer1.company_name)

# --- __str__ from the parent class works for children too (unless overridden) ---
print("\n--- Using inherited __str__ ---")
print(employee1)
print(manager1)
print(developer1)

# --- Putting different types together in one list - a common real pattern ---
all_employees = [employee1, manager1, developer1]

print("\n--- Payroll report (works for ANY employee type) ---")
for emp in all_employees:
    print(f"{emp.name}: {emp.get_salary()}")   # each uses ITS OWN get_salary()


# ============================================================
# Interactive part: add a new employee
# ============================================================
print("\n--- Add a new employee ---")
emp_type = input("Employee type (employee/manager/developer): ").lower()
name = input("Name: ")
emp_id = input("Employee ID: ")
salary = float(input("Base salary: "))

if emp_type == "manager":
    team_size = int(input("Team size: "))
    new_employee = Manager(name, emp_id, salary, team_size)
elif emp_type == "developer":
    language = input("Programming language: ")
    new_employee = Developer(name, emp_id, salary, language)
else:
    new_employee = Employee(name, emp_id, salary)

all_employees.append(new_employee)
new_employee.show_details()