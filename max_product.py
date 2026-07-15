def max_product():
    m = int(input("Enter size of array: "))
    print("Start entering elements (only positive integers) of array, each element in a new line:")
    a = []
    for i in range(m):
        a.append(int(input()))
    b = len(a)
    max = 0
    pairs = []
    for i in range(b):
        for j in range(i):
            if a[i] * a[j] > max:
                max = a[i] * a[j]
                pairs.clear()
                pairs.append(a[i])
                pairs.append(a[j])
    print("Elements that make up the maximum product :", pairs)
    print("Maximum Product is equal to:", max)
max_product()