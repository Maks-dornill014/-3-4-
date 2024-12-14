class Employee:
    def __init__(self, name, position, salary):
       
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
       
        return f"Ім'я: {self.name}, Посада: {self.position}, Зарплата: {self.salary:.2f}"


class Department:
    def __init__(self, name):
       
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        
        self.employees.append(employee)
        print(f"Співробітника {employee.name} додано до відділу '{self.name}'.")

    def remove_employee(self, name):
        
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print(f"Співробітника {name} видалено з відділу '{self.name}'.")
                return
        print(f"Співробітника з ім'ям {name} не знайдено у відділі '{self.name}'.")

    def calculate_total_salary(self):
       
        return sum(employee.salary for employee in self.employees)

    def list_employees(self):
        
        if not self.employees:
            print(f"У відділі '{self.name}' немає співробітників.")
        else:
            print(f"Співробітники у відділі '{self.name}':")
            for employee in self.employees:
                print(f"- {employee}")



if __name__ == "__main__":
    
    it_department = Department("IT")

    
    emp1 = Employee("Олександр", "Програміст", 50000)
    emp2 = Employee("Марія", "Тестувальник", 40000)
    emp3 = Employee("Ігор", "Адміністратор систем", 45000)

   
    it_department.add_employee(emp1)
    it_department.add_employee(emp2)
    it_department.add_employee(emp3)

    
    print("\nСписок співробітників:")
    it_department.list_employees()

    
    it_department.remove_employee("Марія")

    
    print("\nОновлений список співробітників:")
    it_department.list_employees()

    
    total_salary = it_department.calculate_total_salary()
    print(f"\nЗагальна зарплата відділу '{it_department.name}': {total_salary:.2f}")
