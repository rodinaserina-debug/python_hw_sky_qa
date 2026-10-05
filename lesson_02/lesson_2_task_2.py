def is_year_leap(year):
    return True if year % 4 == 0 else False

num_year = int(input("Введите год: "))
result = is_year_leap(num_year)
print(f"Год {num_year}: {result}")