m = list(input("Enter some values:"))
seen = []
for i in m:
    if i not in seen:
        seen.append(i)
print(seen)