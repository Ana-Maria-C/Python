from ex5.Animal import Animal


class Bird(Animal):
    def __init__(self, name, species, breed, feather_color, number_of_legs = 2):
        super().__init__(name, species)
        self.breed = breed
        self.feather_color = feather_color
        self.number_of_legs = number_of_legs

    def make_sound(self, sound):
        print(f"{self.name} says {sound}!")

    def fly(self):
        print(f"{self.name} has {self.number_of_legs} and flies with his wings!")

    def __str__(self):
        return f'{self.name} is a {self.species} of breed {self.breed} with {self.feather_color} feathers.'