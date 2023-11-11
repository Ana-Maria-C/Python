from ex5.Animal import Animal


class Fish(Animal):
    def __init__(self, name, species, breed, scale_color):
        super().__init__(name, species)
        self.breed = breed
        self.scale_color = scale_color

    def make_sound(self, sound):
        print(f"{self.name} says {sound}!")

    def swim(self):
        print(f"{self.name} has no legs and swims with his fins!")

    def __str__(self):
        return f'{self.name} is a {self.species} of breed {self.breed} with {self.scale_color} scales.'