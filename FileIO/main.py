# file = open("my_doc.txt")
with open("my_doc.txt") as file:
    content = file.read()
    print(content)

# file.close()