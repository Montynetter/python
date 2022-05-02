v = [int(s) for s in input().split(' ')]
n = int(input())
for i in range(len(v)):
    if n > v[i]:
        print(i+1)
        break
    elif i == len(v)-1:
        print(len(v)+1)