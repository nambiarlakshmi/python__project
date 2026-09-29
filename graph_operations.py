def count_sink_nodes(graph):
    count = 0

    for node in graph:
        if len(graph[node]) == 0:
            count += 1
    print(count)
graph = {
    1: [2, 3],
    2: [3],
    3: [],
    4: []
}
count_sink_nodes(graph)