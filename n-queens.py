def solveNQueens(n):
    board = [-1] * n
    solutions = []

    def solve(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            safe = True

            for r in range(row):
                if board[r] == col or abs(board[r] - col) == abs(r - row):
                    safe = False
                    break

            if safe:
                board[row] = col
                solve(row + 1)

    solve(0)
    return solutions

print(solveNQueens(8))
#Chat GPT helped me