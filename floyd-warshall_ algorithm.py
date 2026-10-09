def count_paths(graph, start, end):
    if start == end:
        return 1

    count = 0
    for neighbor in graph[start]:
        count += count_paths(graph, neighbor, end)
    return count


graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

start = 'A'
end = 'D'

print("Total paths:", count_paths(graph, start, end))