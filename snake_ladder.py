def snakes_and_ladders(snakes, ladders):
    graph = {}

    for i in range(1, 101):
        graph[i] = [i + 1] if i < 100 else []

    for start, end in snakes.items():
        graph[start] = [end]

    for start, end in ladders.items():
        graph[start] = [end]

    return graph
snakes = {99: 10, 70: 30}
ladders = {5: 25, 20: 60}

board = snakes_and_ladders(snakes, ladders)
print(board[5])
print(board[99])