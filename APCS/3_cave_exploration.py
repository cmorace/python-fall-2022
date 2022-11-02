index = 0
result = 0
vals = [int(x) for x in input().split()]


def dfs():
    global index, result
    parent_val = vals[index]
    for i in range(2 if parent_val % 2 == 0 else 3):
        index += 1
        child_val = vals[index]
        if child_val != 0:
            result += abs(parent_val-child_val)
            dfs()


dfs()
print(result)
