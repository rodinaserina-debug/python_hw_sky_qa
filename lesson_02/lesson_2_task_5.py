def month_to_season(number):
    if 1 <= number <= 2 or number == 12:
        return "Зима"
    if 3 <= number <= 5:
        return "Весна"
    if 6 <= number <= 8:
        return "Лето"
    if 9 <= number <= 11:
        return "Осень"
    return "Неверный номер месяца"

num_month = int(input("Введите номер месяца: "))
print(month_to_season(num_month))
