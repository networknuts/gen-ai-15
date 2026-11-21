file_name = input("Enter file to read: ")

file_content = open(file_name,"r")

for line in file_content.readlines():
    print(line.strip())

file_content.close()