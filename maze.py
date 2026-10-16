def solveMaze(nums, directions):
    pos = 0

    for i in range(len(nums)):
        if directions[i] == '>':
            pos += nums[pos]
        else:
            pos -= nums[pos]

        if pos < 0 or pos >= len(nums):
            return -1

    return pos
print(solveMaze([2, 1, 1, 0], "><><"))
#Chat GPT helped me 