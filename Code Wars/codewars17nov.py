#https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python

# def sum_mix(arr):

#     integers = []
#     count = 0

#     for x in arr:
#         integers.append(int(x))

#     for y in integers:
#         count += y
    
#     return count


# print(sum_mix([9, 3, '7', '3'])) #, 22)
# print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7])) #, 42)
# print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'])) #, 41)






#https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89/train/python

# def mouth_size(animal): 
#     lower = animal.lower()
    
#     return "small" if lower == "alligator" else "wide"


# print(mouth_size("ant bear")) #,"wide")
# print(mouth_size("alligator")) #,"small")






#https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

# def divisible_by(numbers, divisor):

#     new = []

#     for x in numbers:

#         if x % divisor == 0:
#             new.append(x)
#         else:
#             None

#     return new

# print(divisible_by([1,2,3,4,5,6], 3)) #, [3,6])
# print(divisible_by([0,1,2,3,4,5,6], 4)) #, [0,4])
# print(divisible_by([0], 4)) #, [0])
# print(divisible_by([1,3,5], 2)) #, [])





#https://www.codewars.com/kata/56598d8076ee7a0759000087/train/python

# import math 

# def calculate_tip(amount, rating):

#     service = rating.lower()

#     if service == "terrible":
#         return int(0)

#     elif service == "poor":
#         return math.ceil(amount * 0.05)

#     elif service == "good":
#         return math.ceil(amount * 0.1)

#     elif service == "great":
#         return math.ceil(amount * 0.15)
    
#     elif service == "excellent":
#         return math.ceil(amount * 0.2)

#     else:
#         return "Rating not recognised"


# print(calculate_tip(30, "poor")) #, 2)
# print(calculate_tip(20, "Excellent")) #, 4)
# print(calculate_tip(20, "hi")) #, 'Rating not recognised')
# print(calculate_tip(107.65, "GReat")) #, 17)
# print(calculate_tip(20, "great!")) #, 'Rating not recognised')

# BETTER WAYS:
# tips = {
#         'terrible': 0,
#         'poor' : .05,
#         'good' : .1,
#         'great' : .15,
#         'excellent' : .2
#     }
#     if rating.lower() in tips:
#         return ceil(amount * tips[rating.lower()])
#     else:
#         return 'Rating not recognised'





# tip = {
#         "terrible": 0,
#         "poor": 0.05,
#         "good": 0.1,
#         "great": 0.15,
#         "excellent": 0.2
#     }.get(rating)




#https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python

def well(x):

    positive = []

    for rate in x:

        if rate == "good":
            positive.append(rate)

    #print(len(positive))

    if len(positive) == 0:
        return "Fail!"

    elif len(positive) == 1 or len(positive) == 2: 
        return "Publish!"
 
    elif len(positive) > 2:
        return "I smell a series!"



print(well(['bad', 'bad', 'bad'])) #, 'Fail!')
print(well(['good', 'bad', 'bad', 'bad', 'bad'])) #, 'Publish!')
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'])) #, 'I smell a series!')



# BETTER EXAMPLE:
# variable = argument.count("what you want to find") will count how many times it appears

# def well(x):
#     c = x.count('good')
#     return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'