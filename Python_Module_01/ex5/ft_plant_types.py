#!/usr/bin/env python3
class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 age: int) -> None:
        self.name = name.title()
        self.height = height
        self.old = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
        print("=== Flower")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.bloomed is False):
            print(f" {self.name} has not bloomed yet\n"
                  f"[asking the {self.name.lower()} to bloom]")
        else:
            print(f" {self.name} is blooming beautifully!\n")

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
        print("=== Tree")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk:.1f}cm\n"
              f"[asking the {self.name.lower()} to produce shade]")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm",
              f"long and {self.trunk:.1f}cm wide\n")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.season = harvest_season
        self.nutrition = nutritional_value
        print("=== Vegetable")

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.season}\n"
              f" Nutritional value: {self.nutrition}")

    def age(self, days: int) -> None:
        print(f"[make {self.name.lower()} grow and age for {days} days]")
        self.old += days
        self.nutrition += days

    def grow(self, cm: float) -> None:
        self.height += cm


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    flower.bloom()
    flower.show()

    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.produce_shade()

    vege = Vegetable("Tomato", 5, 10, "April", 0)
    vege.show()
    vege.grow(42)
    vege.age(20)
    vege.show()
