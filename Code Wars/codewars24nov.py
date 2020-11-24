#https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

# def sum_str(a, b):

#     #filter(None, [a, b]) - will only return what is true
#     if a == "" or a == None:
#         a = a.replace("", "0")
#     elif b == "" or b == None:
#         b = b.replace("", "0")

#     x = int(a)
#     y = int(b)
#     z = x + y

#     return str(z)

    
# print(sum_str("","34")) #, "39")






# #https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python
# def string_to_array(s):

#     return s.split(" ")
    


# print(string_to_array("Robin Singh")) #, ["Robin", "Singh"])
# print(string_to_array("CodeWars")) #, ["CodeWars"])
# print(string_to_array("I love arrays they are my favorite")) #, ["I", "love", "arrays", "they", "are", "my", "favorite"])
# print(string_to_array("1 2 3")) #, ["1", "2", "3"])
# print(string_to_array("")) #, [""])




#https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/python

def who_is_paying(name):

    x = name[0:2]
    y = [name, x]
    
    if len(name) <= 2:
        return [name]
    else:
        return y



print(who_is_paying("Mexico")) #,["Mexico", "Me"])
print(who_is_paying("Me")) #,["Me"])
print(who_is_paying("")) #, [""])
print(who_is_paying("I")) #, ["I"])
