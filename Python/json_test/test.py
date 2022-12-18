import json

# d = {'a': 1, 'b': 2, 'c': 3}

# s = json.dumps(d)

# with open('Python/json_test/test.json', 'w') as f:
#     f.write(s)

d = None
with open('Python/json_test/test.json', 'r') as f:
    s = f.read()
    d = json.loads(s)

if d is None:
    print("file not found")

print(d)
