# #https://www.codewars.com/kata/5601409514fc93442500010b/train/python

# def better_than_average(class_points, your_points):

# # average and compare

#     average = sum(class_points) / len(class_points)
    
#     return your_points > average
    

# print(better_than_average([2, 3], 5)) # True 
# print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)) #True)
# print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69)) #True)





# #https://www.codewars.com/kata/56f173a35b91399a05000cb7/train/python
# def find_longest(string):
    
#     lower = string.lower()
#     split = lower.split(" ")
    
    
#     organise = sorted(split, key=len)
    
#     return len(organise[-1])


# return max(len(a) for a in strng.split())





    
#     if number < 0:
#         return abs(number)
#     elif number > 0:
#         return -number
#     else:
#         return 0




def get_real_floor(n):
    #return 1 less
    #if 13 return 2 less
    
    if n < 0:
        return n + 1

    elif n > 13:
        return n - 2

    elif n < 13:
        return n - 1

  
print(get_real_floor(1)) #, 0)
print(get_real_floor(5)) #, 4)
print(get_real_floor(15)) #, 13)