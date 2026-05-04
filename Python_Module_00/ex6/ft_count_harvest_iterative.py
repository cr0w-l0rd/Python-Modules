def	ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	count = range(1, days + 1)
	for n in count:
		print(f"Day {n}")
	print("Harvest time!")