def subset_sum(arr, k):
    def find_subset(index, current_sum, subset):
        if current_sum == k:
            return subset
        if current_sum > k or index == len(arr):
            return None
        result = find_subset(index + 1, current_sum + arr[index],
                             subset + [arr[index]])
        if result is not None:
            return result
        return find_subset(index + 1, current_sum, subset)
    return find_subset(0, 0, [])

arr = [2, 3, 7, 8, 10]
k = 10
result = subset_sum(arr, k)
print(result)
#Chat GPT helped me