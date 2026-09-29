def minimum_swaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            correct = arr[i] - 1
            arr[i], arr[correct] = arr[correct], arr[i]
            swaps += 1
    return swaps

arr = [4, 3, 1, 2]
print(minimum_swaps(arr))