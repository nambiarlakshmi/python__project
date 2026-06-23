import math
def pair(arr):
    min = 99999999999999
    answer = []
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if i != j:
                if abs(arr[i] - arr[j]) < min:
                    min = arr[i] + arr[j]
                    answer.clear()
                    answer.append(arr[i])
                    answer.append(arr[j])
                else:
                    pass
            else:
                pass
    print("The closest pair is ", answer[0], " and ", answer[1])
arr = [7, 91, 99, 113, 87, 18, 65, 84, ]
pair(arr)