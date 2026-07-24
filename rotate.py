def rotate(a, m):
    k = len(a)
    while m > 0:
        b = a[k-1]
        a.remove(b)
        a.insert(0,b)
        m -= 1
    print(a)

rotations = int(input("Enter the number of rotations you would like: "))
array = [4, 12, 6, 89, 10, 5]
rotate(array, rotations)