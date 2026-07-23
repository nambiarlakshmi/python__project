def union(a, b):
    result = []

    for x in a:
        if x not in result:
            result.append(x)
    for x in b:
        if x not in result:
            result.append(x)
    return result

def intersection(a, b):
    result = []
    for x in a:
        if x in b and x not in result:
            result.append(x)
    return result

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print("Union:", union(a, b))
print("Intersection:", intersection(a, b))