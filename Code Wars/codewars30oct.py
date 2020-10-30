#https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

# def summation(num):


#     return sum(range(0, num + 1))
    
# print(summation(1)) #, 1)
# print(summation(8)) #, 36)
# print(summation(22)) #, 253)
# print(summation(100)) #, 5050)



# SLICING EXAMPLE

# name = "supacalifragalisticexpilidotious"
# num = 12345

# print(name)

# print(name[2])

# print(name[2:5])

# print(name[::-1]) #slice is only a string method

# change1 = str(num)
# reverse = change1[::-1]
# print(type(int(reverse))) #changing num to string in order to invert it, then changing it back to an integer



#https://www.codewars.com/kata/59ca8246d751df55cc00014c

# def hero(bullets, dragons):

#     return dragons * 2 <= bullets

# print(hero(10, 5)) #, True)
# print(hero(7, 4)) #, False)
# print(hero(4, 5)) #, False)
# print(hero(100, 40)) #, True)


# https://www.codewars.com/kata/55eca815d0d20962e1000106/train/javascript

def hello(name = ""):

    if name == "":
        return "Hello, World!"
    else:
        lower = name.lower()
        new_name = lower[0].upper() + lower[1:]
        return "Hello, " + new_name + "!"

# https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3 - slicing


print(hello("aLiCe"))
print(hello(""))
