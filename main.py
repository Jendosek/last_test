#8
def sort(strings):
    b = []
    for string in strings:
        if string[0].capitalize():
            b.append(string)
    return b
words = input("Введіть рядок: ").split(' ')
res = sort(words)
print(res)

