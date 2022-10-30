A = [[1],
     [1],
     [1],
     [1]]

B = [[1, 1, 1]]

C = [[1, 1],
     [1, 1]]

D = [[0, 0, 1],
     [1, 1, 1]]

E = [[0, 1],
     [1, 1],
     [1, 1]]

SHAPE = {"A": A, "B": B, "C": C, "D": D, "E": E}


def move_left(container, shape, y):
    x = C
    while not is_collision(container, shape, x, y):
        x -= 1
    return x+1


def is_collision(container, shape, x, y):
    # This could be made faster by checking shapes left most ones only
    if x < 0:
        return True
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if j + x >= C:
                continue
            if shape[i][j] == 1 and container[i+y][j+x] == 1:
                return True
    return False


def does_not_fit(shape, x, y):
    return x + len(shape[0]) > C


def place(container, shape, x, y):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == 1:
                # assert(container[y+i][x+j] == 0)
                container[y+i][x+j] = 1


def count_spaces(container):
    spaces = 0
    for i in range(R):
        for j in range(C):
            if container[i][j] == 0:
                spaces += 1
    return spaces


R, C, N = [int(x) for x in input().split()]
goods = [[x for x in input().split()] for _ in range(N)]
container = [C*[0] for _ in range(R)]
discarded_goods = 0
for i in range(N):
    c, y = goods[i][0], int(goods[i][1])
    x = move_left(container, SHAPE[c], y)
    if does_not_fit(SHAPE[c], x, y):
        discarded_goods += 1
    else:
        place(container, SHAPE[c], x, y)

print(count_spaces(container), discarded_goods)
