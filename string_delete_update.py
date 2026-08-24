def replace_character(text, old, new):
    return text.replace(old, new)


def delete_character(text, char):
    return text.replace(char, "")


text = input("Enter a string: ")

text = replace_character(text, "a", "b")
text = delete_character(text, "x")

print(text)