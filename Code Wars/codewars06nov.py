# #https://www.codewars.com/kata/5ce6728c939bf80029988b57/train/python

# import string

# # True = if consecutive and each letter appears once
# # False = otherwise

# def solve(st):
  
#     sort = sorted(st)
#     join = ''.join(sort) 
    
#     alpha = string.ascii_letters
#     return alpha.find(join) != -1

# print(solve("abc")) #,True)
# print(solve("abd")) #, False)
# print(solve("dabc")) #,True)
# print(solve("abbc")) #, False)


def find_multiples(integer, limit):

    multiple = range(1, limit + 1)                    #range(1, limit + 1)
    empty_list = []

    for x in multiple: 

        if integer * x <= limit:
            empty_list.append(integer * x)
            
        elif integer * x > limit:
            None

    return empty_list



   
print(find_multiples(5, 25)) #, [5, 10, 15, 20, 25])
print(find_multiples(1, 2)) #, [1, 2])