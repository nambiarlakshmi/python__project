class Solution:
    def min_flips(arr):
        num_flips = 0
        if arr.count(1) >= arr.count(0):
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = 1
                    num_flips += 1
        else:
            for i in range(len(arr)):
                if arr[i] == 1:
                    arr[i] = 0
                    num_flips += 1
        print(num_flips)
        
arr = [ 0, 1, 1, 0, 0, 0, 1, 1 ]
a = Solution
a.min_flips(arr)