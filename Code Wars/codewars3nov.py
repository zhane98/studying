#https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

# correct = +4
# incorrect = -1
# no answer = 0
#If the score < 0, return 0.
def check_exam(arr1,arr2):

    score = []
    
    for x in range(len(arr1)):

        if arr1[x] == arr2[x]:
            score.append(4)
        
        elif arr2[x] == "":
            score.append(0)
        
        else:
            score.append(-1)

    first = sum(score) if sum(score) >= 0 else 0
    
    return first
    #first = x if y is true else z  

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"])) #, 6)
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""])) #, 7)
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"])) #, 16)
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"])) #, 0)

# def check_exam(arr1,arr2):

#     score = []

#     for x in list(arr1[:-1]) and y in list(arr2[:-1]):

#         if x in arr1[n] == y in arr2[n]:
#             score.append(4)
        
#         elif y in arr2[n] == "":
#             score.append(0)
        
#         else:
#             score.append(-1)


#     return score   