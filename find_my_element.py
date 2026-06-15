def find_element(arr, x):
    arr.sort()
    new_list = arr
    current = 0
    final_index = 0
    m = len(arr)
    for i in range(m // 2 + 1):
        current = len(new_list) // 2
        if new_list[current] == x:
            final_index = current
            break
        elif new_list[current] > x:
            new_list = new_list[0:current:1]
        else:
            new_list = new_list[current::1]
    print("Sorted array is", arr)
    print("Element ", x, " is present at index" , final_index )

b = [82, 32, 45, 77, 63]
c = 63
a = find_element(b, c)