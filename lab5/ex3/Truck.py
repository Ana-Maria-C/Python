from ex3.Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, make, model, year, color, power, weight):
        super().__init__(make, model, year)
        self.color = color
        self.power = power
        self.mileage = 0
        self.weight = weight

    def calculate_mileage(self, distance):
        self.mileage += distance

    def calculate_towing_capacity(self, weight):
        towing_capacity = weight * 0.75
        return towing_capacity

    def print_info(self):
        super().print_info()
        print("Color:", self.color)
        print("Power:", self.power)
        print("Mileage:", self.mileage)
        print("Weight:", self.weight)
        print("Towing capacity:", self.calculate_towing_capacity(self.weight))
