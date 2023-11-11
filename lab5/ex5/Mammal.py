from ex5.Animal import Animal


class Mammal(Animal):
    def __init__(self, name, species, breed, fur_color, number_of_legs = 4):
        super().__init__(name, species)
        self.breed = breed
        self.fur_color = fur_color
        self.number_of_legs = number_of_legs

    def make_sound(self, sound):
        print(f"{self.name} says {sound}!")

    def walk(self):
        print(f"{self.name} walks on {self.number_of_legs} legs")

    def __str__(self):
        return f"{self.name} is a {self.species} of breed {self.breed} with {self.fur_color} fur."
