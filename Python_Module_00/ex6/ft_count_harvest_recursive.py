def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	recursion(days)
	print("Harvest time!")

def	recursion(day):
	if day > 1:
		recursion(day - 1)
	print(f"Day {day}")