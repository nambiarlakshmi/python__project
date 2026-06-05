import array as arr

def find_num(a):
    output = 0
    a = sorted(a)
    for i in range(0, len(a)):
        if i == 0:
            pass
        if a[i] - a[i-1] == 1:
           pass
        else:
            output = a[i] - 1
    print(output)
    
a = arr.array('i',[1, 4, 3, 2, 6])
num = find_num(a)
