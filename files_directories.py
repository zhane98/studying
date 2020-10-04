import os 

# os.mkdir("dummy_folder") # Make Directory
print(os.getcwd()) # current folder that the file is currently in

os.chdir("C:\\Users\zhane\Documents\GitHub\studying\dummy_folder\\") #changing directory/folder, double slashes at beg. and end.

print(os.getcwd()) #to ensure it's changed directories correctly.

file = open("thursday.txt", "x") #creating a new 'thursday' file in the directory we've just changed to. All files created from now on will be saved into the new directory.

# os.rmdir("dummy_folder") # removes a directory

