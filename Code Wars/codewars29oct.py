#https://www.codewars.com/kata/515e271a311df0350d00000f/train/python

# def square_sum(numbers):
#                                             #list comprehension
#     return sum(n ** 2 for n in numbers)     #different to a for loop, as you only want 1 result, so the for loop doesn't work, in this way it returns the 1 answer.


#return sum(map(lambda num : num ** 2, numbers))
    # lambda = def/return, also like the function, num is in the parentheses.
    # after : is like the return bit 
    # map acts like a for loop, so anything after it is iterated


# print(square_sum([1,2])) #, 5)
# print(square_sum([0, 3, 4, 5])) #, 50)



#https://www.codewars.com/kata/582cb0224e56e068d800003c

# import math 

# def litres(time):
    
    # 0.5L per hour
    # given the hours, return amount of water rounded to smallest value
    
    
#     return math.floor(time * 0.5)

#     #return time // 2   - // divides and floors the result.


# print(litres(2)) #, 1, 'should return 1 litre');
# print(litres(1.4)) #, 0, 'should return 0 litres');
# print(litres(12.3)) #, 6, 'should return 6 litres');
# print(litres(0.82)) #, 0, 'should return 0 litres');
# print(litres(11.8)) #, 5, 'should return 5 litres');


#https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python

# import numpy as np

def invert(lst):

    return list(-x for x in lst)




print(invert([1,2,3,4,5])) #,[-1,-2,-3,-4,-5])
print(invert([1,-2,3,-4,5])) #, [-1,2,-3,4,-5])
print(invert([])) #, [])


#def square_sum(numbers):
#                                             
#     return sum(n ** 2 for n in numbers)     

#return sum(map(lambda num : num ** 2, numbers))
    # lambda = def/return, also like the function, num is in the parentheses.
    # after : is like the return bit 
    # map acts like a for loop, so anything after it is iterated