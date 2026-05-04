def ft_water_reminder():
    days = int(input("Days since last watering: "))
    print(f"{'Water the plants!' if days > 2 else "Plants are fine"}")
