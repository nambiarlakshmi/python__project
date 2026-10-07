def can_color(n, edges, m):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    color = [0] * n
    def solve(node):
        if node == n:
            return True
        for c in range(1, m + 1):
            good = True
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    good = False
            if good:
                color[node] = c
                if solve(node + 1):
                    return True
                color[node] = 0
        return False
    return solve(0)


n = 4
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
]
m = 2
print(can_color(n, edges, m))