from ex3.Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color, power):
        super().__init__(make, model, year)
        self.color = color
        self.power = power
        self.mileage = 0

    def calculate_mileage(self, distance):
        self.mileage += distance

    def print_info(self):
        super().print_info()
        print("Color:", self.color)
        print("Power:", self.power)
        print("Mileage:", self.mileage)