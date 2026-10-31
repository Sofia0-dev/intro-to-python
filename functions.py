# functions methods
# print("Hello World")  # built-in function

with open("temp.txt", "w") as file:
    file.write("99.34\n")
    file.write("100\n")
    file.write("54.34\n")

with open("temp.txt", "r") as file:
    content = file.read()
    print(content)


#pip install yt-dlp
 