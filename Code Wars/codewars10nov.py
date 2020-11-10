#https://www.codewars.com/kata/5704aea738428f4d30000914/train/python

# def triple_trouble(one, two, three):

# #first letter of inputs next to eachother
# # return a string 

#     new = ""

#     for x in range(len(one)):
#         new += one[x] + two[x] + three[x]

    
#     return new 


# print(triple_trouble("aaa","bbb","ccc")) #, "abcabcabc")
# print(triple_trouble("aaaaaa","bbbbbb","cccccc")) #, "abcabcabcabcabcabc")
# print(triple_trouble("burn", "reds", "roll")) #, "brrueordlnsl")
# print(triple_trouble("Bm", "aa", "tn")) #, "Batman")


#https://www.codewars.com/kata/5720a1cb65a504fdff0003e2/train/python

# def difference_in_ages(ages):

#     x = sorted(ages)
    
#     return x[0], x[-1], x[-1] - x[0]

# return (min(ages) , max(ages) , max(ages) - min(ages))

# print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88])) #, (3, 88, 85))
# print(difference_in_ages([5, 8, 72, 98, 41, 16, 55])) #, (5, 98, 93))
# print(difference_in_ages([57, 99, 14, 32])) #, (14, 99, 85))


# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
# def zero_fuel(distance_to_pump, mpg, fuel_left):
    
#     return mpg * fuel_left >= distance_to_pump





#https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1/train/python
def array_madness(a,b):

    # empty1 = 0
    # empty2 = 0

    # for x in a:
    #     empty1 += x ** 2

    # for y in b:
    #     empty2 += y ** 3

    # return empty1 > empty2





    m = sum([x ** 2 for x in a])
    o = sum([y ** 3 for y in b])

    return m > o



print(array_madness([4, 5, 6], [1, 2, 3])) #,True)
print(array_madness( [1, 2, 3],[4, 5, 6])) #,False)