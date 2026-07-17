def shell_sort(a):
    n = len(a)
    interval = n//2
    while interval > 0:
        for i in range(interval, n):
            temp = a[i]
            j = i
            while j >= interval and a[j - interval] > temp:
                a[j] = a[j - interval]
                j -= interval

            a[j] = temp
        interval //= 2
    print(a)
numbs = [4, 8, 1, 3, 9, 0, 2]
shell_sort(numbs)
