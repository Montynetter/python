a = int(input()) #ввод двух целочисленных чисел
b = int(input())

if a/b > 3: #сравнение этих двух чисел между собой
    print("1-ое число больше второго более, чем в 3 раза")
elif a < b:
    print("1-ое число меньше второго")
elif a > b:
    print("1-ое число больше второго")