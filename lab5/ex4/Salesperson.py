from ex4.Employee import Employee


class Salesperson(Employee):
    def __init__(self, name, personal_id, phone_number, address, email, date_of_birth, salary, hire_date, company,
                 clients, sales):
        super().__init__(name, personal_id, phone_number, address, email, date_of_birth, salary, hire_date, company)
        self.clients = clients
        self.sales = sales

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def add_sale(self, sale):
        self.sales.append(sale)

    def remove_sale(self, sale):
        self.sales.remove(sale)

    def __str__(self):
        return super().__str__() + f"Clients: {self.clients}\n" \
                                   f"Sales: {self.sales}\n"