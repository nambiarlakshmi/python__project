def sort(a):
    zeroes = []
    ones = []
    twos = []
    for i in range(len(a)):
        if a[i] == 0 :
            zeroes.append(0)
        if a[i] == 1 :
            ones.append(1)
        if a[i] == 2 :
            twos.append(2)
    output = zeroes + ones + twos
    print(output)

a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sorted_num = sort(a)
        