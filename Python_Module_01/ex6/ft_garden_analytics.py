#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.grow_call = 0
            self.age_call = 0
            self.show_call = 0

        def display(self):
            print(f"Stats: {self.grow_call} grow,",
                  f"{self.age_call} age, {self.show_call} show")

    def __init__(self,
                 name: str,
                 height: float,
                 age: int):
        self.name = name.title()
        self.height = height
        self.age = age
        self.stats = self.Statistics()

    @staticmethod
    def check_age(age):
        old = False
        if (age > 365):
            old = True
        print(f"Is {age} days more than a year? -> {old}")

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self, cm):
        self.height += cm
        self.stats.grow_call += 1

    def age_by(self, cm):
        self.age += cm
        self.stats.age_call += 1

    def show(self):
        self.stats.show_call += 1
        print(f"{self.name}: {float(self.height)}cm, {self.age} days old")


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
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk_diameter
        self.shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk:.1f}cm")

    def produce_shade(self) -> None:
        self.shade_calls += 1
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm",
              f"long and {self.trunk:.1f}cm wide.")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self):
        super().bloom()
        self.seeds = 42  # following example


def show_stats(plant):
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.stats.display()
    if hasattr(plant, "shade_calls"):
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
    flower.show()
    show_stats(flower)
    print(f"[asking the {flower.name.lower()} to grow and bloom]")
    flower.grow(8)
    flower.bloom()
    flower.show()
    show_stats(flower)

    print("\n=== Tree")

    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    show_stats(tree)
    print(f"[asking the {tree.name.lower()} to produce shade]")
    tree.produce_shade()
    show_stats(tree)

    print("\n=== Seed")

    seed = Seed("Sunflower", 80, 45, "yellow")
    seed.show()
    print(f"[make {seed.name.lower()} grow, age and bloom]")
    seed.grow(30)
    seed.age_by(20)
    seed.bloom()
    seed.show()
    show_stats(seed)

    print("\n=== Anonymous")

    anonymous = Plant.anonymous()
    anonymous.show()
    show_stats(anonymous)
