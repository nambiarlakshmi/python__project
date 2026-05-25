def allsubstring(arr, SetSize):

    for outer in range(0, 1 << SetSize):
        for inner in range(0, SetSize):
            if (outer & (1 << inner)) > 0:
                print(arr[inner], end="")
        print()

size = int(input("Enter array size : "))
arr = []
for i in range(size):
    n = input("Enter element : ")
    arr.append(n)

allsubstring(arr, len(arr))

# Ma'am I was stuck on this code so use ChatGPT for help and some parts from another code we did that is similar to this one.