with open("test5.txt","r+") as file:
    content = file.read()
    print(content)
    file.write("\nThis is new content")