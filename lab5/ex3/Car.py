from ex3.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make, model, year, color, power, seats):
        super().__init__(make, model, year)
        self.color = color
        self.power = power
        self.seats = seats
        self.mileage = 0

    def calculate_mileage(self, distance):
        self.mileage += distance

    def print_info(self):
        super().print_info()
        print("Color:", self.color)
        print("Power:", self.power)
        print("Seats:", self.seats)
        print("Mileage:", self.mileage)