# A community garden needs to know the area of a rectangular plot. Write a function
# named ft_plot_area that asks for length and width, then calculates and displays the
# area.
# >>> ft_plot_area()
# Enter length: 5
# Enter width: 3
# Plot area: 15

def ft_plot_area():
	length = int(input("Enter length: "))
	width = int(input("Enter width: "))
	print(f"Plot area: {length * width}")