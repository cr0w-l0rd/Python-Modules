#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.old = age
    
    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        

if __name__ == "__main__":
    plants = [Plant("Rose", 25.0, 30),
              Plant("Rose", 25.0, 30),
              Plant("Rose", 25.0, 30),
              Plant("Rose", 25.0, 30),
              Plant("Rose", 25.0, 30)]
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()
    


