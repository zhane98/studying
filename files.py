import os

file = open("blank.txt", "a")
file.write(" sunday, monday")
file.close()

file = open("blank.txt", "r")
print(file.read())

for line in file:
    print(line)

#file = open("tuesday", "x")
#file.close()
#os.rename("sunday.txt", "monday.txt")
#os.remove("monday.txt")
#os.remove("tuesday")

path = "tuesday.txt"

if os.path.exists(path):
    os.remove(path)
else:
    file = open(path, "x")


new_path = "wednesday.txt"

if os.path.exists(new_path):
    os.remove(new_path)
else:
    print("The file " + "'" + new_path + "'" + " does not exist")