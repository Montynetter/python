s=0
v=input().split(' ')
for i in range(1,len(v)-1):
    if float(v[i])>float(v[i-1]) and float(v[i])>float(v[i+1]):
        s+=1
print(s)