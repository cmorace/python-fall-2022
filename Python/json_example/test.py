import json


def write_json(path: str, d: dict[any, any]):
    s = json.dumps(d)
    with open(path, 'w') as f:
        f.write(s)


def read_json(path: str) -> dict[any, any] | None:
    with open(path, 'r') as f:
        s = f.read()
        return json.loads(s)


write_json("Python/json_example/test.json", {"a": 1, "b": 2})
print(read_json("Python/json_example/test.json"))
