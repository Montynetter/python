a = float(input("vvedite pervoe 4islo "))
b = float(input("vvedite vtoroe 4islo "))
opration = [input("vvedite operaciu ")]
plus = ["+"]
minus = ["-"]
multiply = ["*"]
divide = ["/"]

if opration[0] == plus[0]:
    print(a + b)

elif opration[0] == minus[0]:
    print(a - b)

elif opration[0] == multiply[0]:
    print(a * b)

elif opration[0] == divide[0]:
    print(a / b)

elif opration[0]:
    print("Unknown operation")
