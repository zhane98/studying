# def quarter_of(month):


#     if month == 1 or month == 2 or month == 3:
#         return 1
#     elif month == 4 or month == 5 or month == 6: 
#         return 2
#     elif month == 7 or month == 8 or month == 9:
#         return 3
#     elif month == 10 or month == 11 or month == 12:     use range instead, or ceil function in math
#         return 4

# print(quarter_of(3)) #1)
# print(quarter_of(8)) #3)

from collections import Counter

def repeats(arr):

    occurences = Counter(arr)

    new_list = []   

    for key, value in occurences.items():           #LIST COMPREHENSION = return sum([x for x in arr if arr.count(x) == 1])

        if value == 1:
            new_list.append(key)

    
    return sum(new_list)
            

print(repeats([4,5,7,5,4,8])) #,15) - 7, 8
print(repeats([9, 10, 19, 13, 19, 13])) #,19) - 9, 10