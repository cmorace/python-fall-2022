from collections import deque
N = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]


def get_shortest_path(height_limit: int) -> int:
    # bfs
    q = deque()
    q.append((0, 0))
    next_step_q = deque()
    steps = 0
    is_visited = [N*[False] for _ in range(N)]
    while q:
        i, j = q.popleft()
        is_visited[i][j] = True
        current_height = grid[i][j]
        neighbors = ((i, j+1), (i-1, j), (i, j-1), (i+1, j))
        valid_neighbors = [(i, j) for i, j in neighbors
                           if 0 <= i < N and 0 <= j < N
                           and not is_visited[i][j]
                           and abs(grid[i][j]-current_height) <= height_limit]
        for n in valid_neighbors:
            next_step_q.append(n)
            if n[0] == N-1 and n[1] == N-1:
                return steps + 1
        if len(q) == 0:
            q = next_step_q
            next_step_q = deque()
            steps += 1
    return -1


# min_steps = 2*N
# MAX_HEIGHT = 10
# max_height = MAX_HEIGHT
# for current_height in range(MAX_HEIGHT, -1, -1):
#     shortest_path = get_shortest_path(current_height)
#     if shortest_path < 0:
#         break
#     max_height = current_height
#     min_steps = shortest_path

max_height = 100
min_height = 0
while min_height < max_height:
    mid = (min_height + max_height) // 2
    shortest_path = get_shortest_path(mid)
    if shortest_path < 0:
        min_height = mid + 1
    else:
        max_height = mid
        min_steps = shortest_path

print(max_height)
print(min_steps)
