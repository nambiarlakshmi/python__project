def count_trees(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * n
    trees = 0

    def dfs(node):
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                dfs(next_node)

    for i in range(n):
        if not visited[i]:
            trees += 1
            dfs(i)

    return trees
n = 6
edges = [
    (0, 1),
    (1, 2),
    (3, 4)
]
print(count_trees(n, edges))