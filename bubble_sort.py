def bubble_sort():
    m = int(input("Enter size of array: "))
    print("Start entering elements of array, each element in a new line:")
    a = []
    for i in range(m):
        a.append(int(input()))
    b = len(a)
    for i in range(b):
        for j in range(b-i-1):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print("Sorted Array:")
    print(a)

bubble_sort()