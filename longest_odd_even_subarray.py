is_even = ''
is_odd = ''
def find_(a):
    max_val = 0
    current = 0
    last_was = ''
    c = len(a)
    d = len(a) -1
    for i in range(c):
        for j in range(d):
            if j == 0:
                if even(a[i]) == 'even':
                    last_was = 'even'
                    current += 1
                else:
                    last_was = 'odd'
                    current += 1
            else:
                if last_was == 'odd':
                    if even(a[i]) == even:
                        last_was = 'even'
                        current += 1
                    else:
                        if current > max_val:
                            max_val = current
                            current = 0
                else:
                    if odd(a[i]) == 'odd':
                        last_was = 'odd'
                        current += 1
                    else:
                            if current > max_val:
                                max_val = current
                                current = 0
    print(max_val)

def even(b):
    if b % 2 == 0:
        return 'even'
    else:
        return 'odd'
def odd(b):
    if b % 2 == 0:
        return 'odd'
    else:
        return 'even'

a = [6,4,9,4,7,2,3,4,2,52]
even_odd = find_(a)