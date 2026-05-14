#!/usr/bin/env python3

#!/usr/bin/env python3
class Plant:
    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display_stats(self):
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")
    def __init__(self,
                 name: str,
                 height: float,
                 age: int) -> None:
        self.name = name.title()
        self.height = height
        self.old = age
        self.stats = self.Stats()


    def show(self) -> None:
        self.tats.show_count += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")

    @staticmethod
    def check_old(age) -> bool:
        if (age > 365):
            return True
        return False

    @classmethod
    def anonymous(self) -> None:
        self.name = 'Unknown plant'
        self.show()


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


class Seed(Flower):
    def __init__(self, name : str, seed_num : str):
        super().__init__(name)
        self.seeds = seed_num


if __name__ == "__main__":

    rando_plant1 = Plant('meow', 12, 30)
    rando_plant2 = Plant('bark', 12, 400)


    print("=== Garden Plant Types ===")

    print("=== Check year-old")

    print(f"Is {rando_plant1.old} days more than a year? {rando_plant1.check_old(rando_plant1.old)}")
    print(f"Is {rando_plant2.old} days more than a year? {rando_plant2.check_old(rando_plant2.old)}")

    print("=== Flower")
    rose = Flower('rose', 15, 10, 'red')
    rose.show()
    rose.Stats.show_stats()
