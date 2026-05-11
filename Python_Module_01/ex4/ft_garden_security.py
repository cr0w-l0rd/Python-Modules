#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = height
        self._old = age

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._old} days old")

    def set_height(self, height) -> int:
        if (height >= 0):
            self._height = height
        else:
            return 0
        return 1

    def set_age(self, age) -> int:
        if (age >= 0):
            self._old = age
        else:
            return 0
        return 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._old


if __name__ == "__main__":
    plants = Plant("Rose", 25.0, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {plants.name}: {plants.get_height()}cm,",
          f"{plants.get_age()} days old\n")
    updated_height = plants.set_height(-1)
    updated_age = plants.set_age(-100)
    if (updated_height == 1):
        print(f"Height updated: {plants.get_height()}cm")
    else:
        print(f"{plants.name}: Error, height can't be negative\n"
              "Height update rejected")
    if (updated_age == 1):
        print(f"Age updated: {plants.get_age()} days\n")
    else:
        print(f"{plants.name}: Error, age can't be negative\n"
              "Age update rejected\n")
    print(f"Current state: {plants.name}: {plants.get_height():.1f}cm,",
          f"{plants.get_age()} days old")
