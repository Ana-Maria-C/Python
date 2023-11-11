from ex4.Employee import Employee


class Manager(Employee):
    def __init__(self, name, personal_id, phone_number, address, email, date_of_birth, salary, hire_date, company,
                 employees: list[Employee], department):
        super().__init__(name, personal_id, phone_number, address, email, date_of_birth, salary, hire_date, company)
        self.department = department
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        self.tasks = dict.fromkeys(employees, [])

    def add_employee(self, employee):
        self.employees.append(employee)
        self.tasks[employee] = []

    def remove_employee(self, employee):
        self.employees.remove(employee)
        del self.tasks[employee]

    def assign_tasks(self, employee, task):
        self.tasks[employee].append(task)

    def __str__(self):
        employee_str = "\n".join(map(str, self.employees))
        return super().__str__() + f"Department: {self.department}\n" \
                                   f"Employees: \n {employee_str}\n"
