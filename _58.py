import json

with open('file_56.json', 'r') as file:
    d = json.load(file)

d['employees'].append({'firstName': 'Albert', 'lastName': 'Bert'})
print(d)

with open('file_56.json', 'w') as file:
    file.write(json.dumps(d, indent=4))
