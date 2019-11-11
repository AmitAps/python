principle = float(input('Enter the principle (Initial investment): '))
rate = float(input('Enter the rate of interest :'))
time_compounded = float(input('Enter the number of times the interest is compounded per year: '))
time_for_years = float(input("Enter the number of years: "))

amount = principle * ((1 + (rate / (100.0 * time_compounded))) ** (time_compounded * time_for_years))

print(amount)
