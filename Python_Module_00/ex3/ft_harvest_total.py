# A gardener harvested vegetables on three
# different days. Write a function named ft_harvest_total
# that asks for the weight of each
# harvest and calculates the total.
# >>> ft_harvest_total()
# Day 1 harvest: 5
# Day 2 harvest: 8
# Day 3 harvest: 3
# Total harvest: 16

def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day1 + day2 + day3}")
