text = input("Enter a string: ")
count = {}

for char in text:
    count[char] = count.get(char, 0) +1
for char in text:
    if count[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating characters")