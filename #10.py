a = []
b = []
for i in range(8):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if abs(a[i] - a[j]) == abs(b[i] - b[j]) or (a[i] == a[j]) or (b[i] == b[j]):
            print("NO")
            exit()
print("YES")