i = 0
c = []
f = []
r = ["с"]
a = input()

for i in range(0, len(a), 1):
    b = a[i]
    if i != 2:
        c.append(b)
    if b == r[0]:
        print('Есть символ "c"')
    if i < len(a) - 1:
        f.append(b)

print("Пропущен 3-й символ: " + "".join(c))
print("Длинна строки: " + str(len(a)))
print("Пропущен последний символ: " + "".join(f))

