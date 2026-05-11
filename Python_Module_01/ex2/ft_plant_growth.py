#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.old = age
    
    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")

    def grow(self, cm: float) -> None:
        self.height += cm

    def age(self) -> None:
        self.old += 1
        

if __name__ == "__main__":
    plant1 = Plant("rose", 0, 0)
    start_height: float = plant1.height
    print("=== Garden Plant Registry ===")
    plant1.show()
    for i in range(1,8):
        print(f"=== Day {i} ===")
        plant1.grow(0.8)
        plant1.age()
        plant1.show()
    print(f"Growth this week: {plant1.height - start_height:.1f}cm")
        
    