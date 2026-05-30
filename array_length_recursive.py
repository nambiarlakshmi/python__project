def arr(a, b=0):
    if len(a) == 0:
        print("Lenght of array: ", b)
    else:
        a.pop(0)
        b+=1
        arr(a,b)

a = [1,2,234,234,745,3,6,653]
ar = arr(a)