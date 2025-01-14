class Employee:
    """
    Class to represent an employee.
    """
    def __init__(self, emp_id, name, age, position, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.department = department

    def update_info(self, **kwargs):
        """
        Update employee information.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def display_info(self):
        """
        Display employee information.
        """
        return f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}, Department: {self.department}"


class EmployeeManagementSystem:
    """
    Class to manage employees.
    """
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, age, position, salary, department):
        """
        Add a new employee to the system.
        """
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
        else:
            self.employees[emp_id] = Employee(emp_id, name, age, position, salary, department)
            print(f"Employee {name} added successfully.")

    def remove_employee(self, emp_id):
        """
        Remove an employee from the system.
        """
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee with ID {emp_id} removed successfully.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def update_employee(self, emp_id, **kwargs):
        """
        Update an existing employee's information.
        """
        if emp_id in self.employees:
            self.employees[emp_id].update_info(**kwargs)
            print(f"Employee with ID {emp_id} updated successfully.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def display_all_employees(self):
        """
        Display all employees in the system.
        """
        if self.employees:
            for emp in self.employees.values():
                print(emp.display_info())
        else:
            print("No employees in the system.")

# Example Usage
if __name__ == "__main__":
    system = EmployeeManagementSystem()

    # Adding employees
    system.add_employee(1, "Alice", 30, "Engineer", 75000, "R&D")
    system.add_employee(2, "Bob", 40, "Manager", 90000, "Sales")

    # Display all employees
    print("\nAll Employees:")
    system.display_all_employees()

    # Update an employee's info
    system.update_employee(1, age=31, salary=77000)

    # Display updated employee info
    print("\nUpdated Employee:")
    print(system.employees[1].display_info())

    # Remove an employee
    system.remove_employee(2)

    # Display all employees after removal
    print("\nAll Employees After Removal:")
    system.display_all_employees()