#https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python

# def row_weights(array):

#     group1 = []
#     group2 = []

#     for x in range(len(array)):

#         if x % 2 == 0:
#             group1.append(array[x])

#         else:
#             group2.append(array[x])

#     sum1 = sum(group1)
#     sum2 = sum(group2)

#     return (sum1, sum2)


# print(row_weights([80])) #, (80,0))
# print(row_weights([100,50])) #, (100,50))
# print(row_weights([50,60,70,80])) #, (120,140))
# print(row_weights([13,27,49])) #, (62,27))
# print(row_weights([70,58,75,34,91])) #, (236,92))
# print(row_weights([29,83,67,53,19,28,96])) #, (211,164))
# print(row_weights([0])) #, (0,0))
# print(row_weights([100,51,50,100])) #, (150,151))
# print(row_weights([39,84,74,18,59,72,35,61])) #, (207,235))
# print(row_weights([0,1,0])) #, (0,1))


# OTHER SOLUTION:

# def row_weights(array):
#     return sum(array[::2]), sum(array[1::2]) #start from 0 in steps of 2



#https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python

def solve(word):

#split string into individual characeters in a list 
#truthy:  if letter in xyz == letter.upper()
#append to list1 (all of the uppers)
#else: append to list2 (all of the lowers)
#compare length of lists 

    list1 = [] #upper
    list2 = [] #lower

    for letter in word:
        
        if letter == letter.upper():
            list1.append(letter)
        else:
            list2.append(letter)

    if len(list1) > len(list2):
        return word.upper()
    else:
        return word.lower()


print(solve("code")) #,"code")
print(solve("CODe")) #,"CODE")
print(solve("COde")) #,"code")
print(solve("Code")) #,"code")