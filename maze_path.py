n = int(input("Enter number of rows : "))
m = int(input("Enter number of columns : "))

def maze(x, y, path):
    matrix = [[0 for column in range(m)]
                  for rows in range(n)]

    if x == n - 1 and y == m - 1:
        print(path)
        return

    if x < n - 1:
        maze(x + 1, y, path + "d")

    if y < m - 1:
        maze(x, y + 1, path + "r")

maze(0, 0, "")

# Ma"am, I was having a hard time with this code so I used ChatGPT