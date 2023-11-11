from ex5.Bird import Bird
from ex5.Fish import Fish
from ex5.Mammal import Mammal

def main():
    dog = Mammal("Rex", "dog", "labrador", "brown")
    dog.make_sound("woof-woof")
    dog.walk()
    print(dog)
    print()

    fish = Fish("Nemo", "fish", "clownfish", "orange")
    fish.make_sound("blub-blub")
    fish.swim()
    print(fish)
    print()

    bird = Bird("Tweety", "bird", "canary", "yellow")
    bird.make_sound("chirp-chirp")
    bird.fly()
    print(bird)


if __name__ == '__main__':
    main()
