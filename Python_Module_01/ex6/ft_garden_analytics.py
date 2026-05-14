#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.grow_call = 0
            self.age_call = 0
            self.show_call = 0
        
        def display(self):
            print(f"[statistics for {self.name}]",
                  f"Stats: {self.grow_call} grow, {self.age_call} age, {self.show_call} show")
    def __init__(self,
                 name: str,
                 height: float,
                 age: int) -> None:
        self.name = name.title()
        self.height = height
        self.old = age
        self.stats = self.Statistics()

    @staticmethod
    def check_age(age):
        old = False
        if (age > 365):
            old = True
        print(f"Is {age} days more than a year? -> {old}")

    @classmethod
    def anonymous(cls):
        print(f"Unknown plant: 0.0cm, 0 days old")
    
    def grow(self):
        self.height += cm
        self.stats.grow_call += 1

    def age_by(self, days):
        self.age += days
        self.stats.age_call += 1

    def show(self):
        self.stats.show_call += 1
        print(f"{self.name}: {float(self.height)}cm, {self.old} days old")


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.bloomed is False):
            print(f" {self.name} has not bloomed yet\n")
        else:
            print(f" {self.name} is blooming beautifully!\n")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.bloomed = True


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk:.1f}cm\n"
              f"[asking the {self.name.lower()} to produce shade]")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm",
              f"long and {self.trunk:.1f}cm wide\n")


def show_stats(plant):
    print(f"[statistics for {plant.name.capitalize()}]")
    plant._stats.display()
    if hasattr(plant, "_shade_calls"):
        print(f" {plant.shade_calls} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")

    Plant.check_age(30)
    Plant.check_age(400)

    print("\n=== Flower")

    # Rose: 15.0cm, 10 days old
    # Color: red
    # Rose has not bloomed yet

    flower = Flower("Rose", 15, 10, "red")
    someplant = Plant("meow", 1,1)
    flower.show()
    flower.bloom()
    flower.show()
    someplant.stats.display()

    print("\n=== Tree")

    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.produce_shade()

    print("\n=== Seed")
    
    print("\n=== Anonymous")
