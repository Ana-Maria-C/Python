class Employee:
    def __init__(self, name, personal_id, phone_number, address, email, date_of_birth, salary, hire_date, company):
        self.name = name
        self.personal_id = personal_id
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.date_of_birth = date_of_birth
        self.salary = salary
        self.hire_date = hire_date
        self.company = company

    def give_raise(self, amount):
        self.salary += amount

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Personal ID: {self.personal_id}\n" \
               f"Phone number: {self.phone_number}\n" \
               f"Address: {self.address}\n" \
               f"Email: {self.email}\n" \
               f"Date of birth: {self.date_of_birth}\n" \
               f"Salary: {self.salary}\n" \
               f"Hire date: {self.hire_date}\n" \
               f"Company: {self.company}\n"