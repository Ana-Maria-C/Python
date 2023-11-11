from ex3.Truck import Truck
from ex3.Car import Car
from ex3.Motorcycle import Motorcycle


def main():
    car = Car("Toyota", "Corolla", 2015, "red", 1.8, 5)
    car.calculate_mileage(100)
    car.print_info()
    print()

    truck = Truck("Ford", "F-150", 2018, "black", 5.0, 2000)
    truck.calculate_mileage(100)
    truck.print_info()
    print()

    motorcycle = Motorcycle("Honda", "CBR", 2017, "black", 1.0)
    motorcycle.calculate_mileage(100)
    motorcycle.print_info()


if __name__ == "__main__":
    main()
