#https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python

# def remove_every_other(my_list):

#     empty = []

#     for x in range(len(my_list)): 
        
#         if x % 2 == 0:           #Odd
#             empty.append(my_list[x])
    
#     return empty


#     return my_list[::2]


# print(remove_every_other(['Hello', 'Goodbye', 'Hello Again'])) #, ['Hello', 'Hello Again'])
# print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #[1, 3, 5, 7, 9])
# print(remove_every_other([[1, 2]])) #, [[1, 2]])
# print(remove_every_other([['Goodbye'], {'Great': 'Job'}])) #[['Goodbye']])



#https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python

# def get_grade(s1, s2, s3):

#     mean = (s1 + s2 + s3) / 3
    
#     if 90 <= mean <= 100:
#         return "A"
#     elif 80 <= mean <= 90:
#         return "B"
#     elif 70 <= mean <= 80:
#         return "C"
#     elif 60 <= mean <= 70:
#         return "D"
#     elif 0 <= mean <= 60:
#         return "F"

# print(get_grade(95, 90, 93)) #, "A"
# print(get_grade(75, 70, 79)) #, "C"
# print(get_grade(58, 59, 60)) #, "F"


#https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python

def no_boring_zeros(n):

    # for n:
    #     if n % 10 != 0:
    #         print(n)


    #         #if True, go through the loop aganin 
    #         #if False, return it 

    a = str(n).rstrip("0") #rstrip = right, lstrip = left, strip = anywhere
    
    if n == 0:
        return 0
    
    else: 
        return int(a)


print(no_boring_zeros(1050)) #, 105)
print(no_boring_zeros(-1050)) #, -105)
print(no_boring_zeros(0)) #, 0)