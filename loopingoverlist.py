my_list = ["dave", "sam", "simon", "tammy", "almudena"]

# 1
for x in my_list: # == ["dave", "sam", "simon", "tammy", "almudena"]
    print(x) # "dave"....

# 2
for x in range(len(my_list)): # == [0, 1, 2, 3, 4]
    print(my_list[x]) # "dave"....
    print(x) # 0....

# 3
for index, name in enumerate(my_list):
    
    # [0, 1, 2, 3, 4]
    # ["dave", "sam", "simon", "tammy", "almudena"]

    print(f'x is = to {index}, nam is = to {name}')