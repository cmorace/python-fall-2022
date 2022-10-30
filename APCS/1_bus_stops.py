def manhattan_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])


N = int(input())
stops = [[int(x) for x in input().split()] for _ in range(N)]
distance = [manhattan_distance(stops[i], stops[i+1]) for i in range(N-1)]
print(max(distance), min(distance))
