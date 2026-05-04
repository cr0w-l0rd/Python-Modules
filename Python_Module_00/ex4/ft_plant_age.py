# Write a function named ft_plant_age that
# asks for a plant’s age in days and tells you
# whether it’s ready to harvest
# (strictly more than 60 days) or not.
# >>> ft_plant_age()
# Enter plant age in days: 75
# Plant is ready to harvest!
# >>> ft_plant_age()
# Enter plant age in days: 45
# Plant needs more time to grow.

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    print(f"Plant {'is ready to harvest!' if age > 60
                   else 'needs more time to grow.'}")
