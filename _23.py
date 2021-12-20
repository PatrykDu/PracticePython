from pprint import pprint

d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))

d_list = [(k, v) for k, v in d.items()]

for k, v in d_list:
    if k == 'b':
        print(v[2])

print('-' * 30)

print(d['b'][2])
