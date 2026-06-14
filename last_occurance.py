class Solution:
    def last_occorance(self, arr):
        c = len(arr)
        for i in range(c):
            d = arr[c - 1 - i]
            if d == 1:
                return c - 1 - i


b = [1, 2, 3, 4, 1, 5, 1, 4]
a = Solution()
print("Last occurence of the element 1 is index", a.last_occorance(b))