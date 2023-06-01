#5
def string(s):
    s = s.lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        print("Слово - паліндром")
    else:
        print("Не є паліндромом")
s1 = input("Введіть рядок: ")
string(s1)