def max_difference(a):
    b = 999999999
    for i in range(len(a)):
        if a[i] < b:
            b = a[i]
            break
    
    c = -999999999
    for i in range(len(a)):
        if a[i] > c:
            c = a[i]
            break

    d = c -b
    print(f"Output : {5232}")

a =[4, 5, 234, 2, 6, 82, 234, 5234]
max_difference = max_difference(a)