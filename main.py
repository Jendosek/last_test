#2
a = int(input("Введіть перше число діапазону: "))
b = int(input("Введіть друге число діапазону: "))
summ = 0
for i in range(a, b+1):
    summ += i
print(f"Сума чисел в діапазоні становить: {summ}")