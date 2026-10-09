def is_sum_string(s):
    n = len(s)

    for i in range(1, n):
        for j in range(i + 1, n):
            a = s[:i]
            b = s[i:j]

            while j < n:
                total = str(int(a) + int(b))

                if not s.startswith(total, j):
                    break

                j += len(total)
                a = b
                b = total

            if j == n:
                return True

    return False


s = input("Enter a string: ")
print(is_sum_string(s))