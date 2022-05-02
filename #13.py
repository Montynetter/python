d = {}
while True:
    try:
        c, t, v = input().split()
        if c not in d:
            d[c] = {t:int(v)}
        else:
            if t not in d[c]:
                d[c][t] = int(v)
            else:
                d[c][t] += int(v)
    except:
        break
for c in sorted(d.items()):
    print(c[0] +":", *[k +' '+str(v) for k, v in sorted(c[1].items())], sep='\n')
