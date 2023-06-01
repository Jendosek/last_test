#9
def sort(strings):
    b = []
    for string in strings:
        if string == "Python":
            return string
    return b
words = input("Введіть рядок: ").split(' ')
res = sort(words)
print(res)

