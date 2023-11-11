from ex4.Manager import Manager
from ex4.Salesperson import Salesperson
from ex4.Engeneer import Engineer
from ex4.Employee import Employee


def main():
    employee = Employee("Ana", "123456739", "0752345678", "acasa", "ana@yahoo.com", "02/08/2000", None, None,None)
    manager = Manager("Maria", "123456789", "0752345678", "acasa", "maria@yahoo.com", \
                      "01/01/1990", 10000, "01/01/2010", "Amazon", [], "IT")
    manager.add_employee(employee)
    manager.assign_tasks(employee, "Tema Python")
    manager.assign_tasks(employee, "Tema ML")
    print(manager)
    print(employee)
    print()

    salesperson = Salesperson("Maria", "123456789", "0752345678", "acasa", "maria@yahoo.com", \
     "01/01/1990", 10000, "01/01/2010", "Amazon", [], [])
    salesperson.add_client("client1")
    salesperson.add_client("client2")
    salesperson.add_sale("sale1")
    salesperson.add_sale("sale2")
    print(salesperson)
    print()

    engineer = Engineer("Alex", "123456789", "0752345678", "acasa", "constantin@yahoo.com", \
    "01/01/1990", 10000, "01/01/2010", "Amazon", [], [])
    engineer.add_project("project1")
    engineer.add_project("project2")
    engineer.add_new_known_language("Python")
    engineer.add_new_known_language("Java")
    print(engineer)
    print()


if __name__ == "__main__":
    main()

