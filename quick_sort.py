def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
arr = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(arr))

# I used the sudocode in the notes to make my code