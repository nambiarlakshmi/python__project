def findPaths(grid):
    n = len(grid)
    m = len(grid[0])
    paths = []

    def dfs(r, c, path, found):
        if r >= n or c >= m:
            return

        if grid[r][c] == 0:
            return

        found = found or grid[r][c] == -1
        path.append((r, c))

        if r == n - 1 and c == m - 1:
            if found:
                paths.append(path[:])
        else:
            dfs(r + 1, c, path, found)
            dfs(r, c + 1, path, found)

        path.pop()

    dfs(0, 0, [], False)
    return paths
print(findPaths([
    [1, -1, 1],
    [1,  1, 1],
    [0,  1, 1]
]))
#Chat GPT helped me