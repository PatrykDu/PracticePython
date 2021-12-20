d = {}
keys = ['a', 'b', 'c']
v = 1
for key in keys:
    values = []
    for i in range(10):
        values.append(v)
        v += 1
    d[key] = values

print(d)
