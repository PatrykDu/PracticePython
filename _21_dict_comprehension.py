d = {"a": 1, "b": 2, "c": 3}

# d_filtered = {}
# for (key, value) in d.items():
#     if value <= 1:
#         d_filtered[key] = value

d_filtered = dict((k, v) for k, v in d.items() if v <= 1)

print(d_filtered)
