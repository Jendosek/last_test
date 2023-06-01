#7
dict = {}
b = ''
while b != "q":
    key = input(f"Введіть ім'я студента: ")
    value = input(f"Введіть оцінку з математики: ")
    dict[key] = value
    a = max(value)
    b = input("Для виходу натисніть q ")
    print()
    print(dict)
    print(f"Максимальне значення зі словника: {a}")
    print()
    continue
