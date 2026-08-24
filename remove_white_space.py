def remove_whitespace(text):
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    return text


text = input("Enter a string: ")

print(remove_whitespace(text))