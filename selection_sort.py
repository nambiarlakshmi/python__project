def selection_sort():
    m = int(input("Enter size of array: "))
    print("Start entering elements of array, each element in a new line:")
    a = []
    for i in range(m):
        a.append(int(input()))
    b = len(a)
    c = []
    for i in range(b):
        c.append(min(a))
        a.remove(min(a))
    print("Sorted Array:")
    print(c)
selection_sort()