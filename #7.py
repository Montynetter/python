a = 100
for i in range(a):
    a = a - 1
    g = 100 - a
    if g%10 == 1 and g != 11:
        print("Упала " + str(g) + " бутылка")
    elif g == 12 or g == 13 or g == 14:
        print("Упало " + str(g) + " бутылок")
    elif g%10 == 2 or g%10 == 3 or g%10 ==  4 :
        print("Упало " + str(g) + " бутылки")
    else:
        print("Упало " + str(g) + " бутылок")
