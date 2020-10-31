#https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python

# import math

# def get_average(marks):
    
#     return math.floor(sum(marks) / len(marks))


# print(get_average([2, 2, 2, 2])) #, 2, "didn't work for [2, 2, 2, 2]")
# print(get_average([1, 5, 87, 45, 8, 8]), 25, "didn't work for [1, 5, 87, 45, 8, 8]")
# print(get_average([2,5,13,20,16, 16,10]), 11, "didn't work for [2,5,13,20,16,16,10]")


#https://www.codewars.com/kata/57089707fe2d01529f00024a/train/python

# def check_alive(health):

#     if health <= 0: 
#         return False
#     else:
#         return True



# print(check_alive(-2)) #, False)
# print(check_alive(0)) #, False)
# print(check_alive(1)) #, True)
# print(check_alive(3)) #, True)


# # https://www.codewars.com/kata/55eea63119278d571d00006a/train/python
# def next_id(arr):

#     # ran = list(range(arr))
#     # return x in ran if x not in arr

# # temp_array = [5, 2, 7, 9]
# # sorted_array = temp_array.sort()
# # print(sorted_array)
    

# # s = [ i  for i in range(20) if i not in myarray ]

# # limit = 20
# # myarray = [1, 5, 15]  # Example
# # missingNumbers = list(set(range(1, limit + 1)) - set(myarray))

#     for i in range(len(arr)+1):
    
#         if i not in arr:
#             return i

# print(next_id([0,1,2,3,4,5,6,7,8,9,10])) #, 11)
# print(next_id([5,4,3,2,1])) #, 0)
# print(next_id([0,1,2,3,5])) #, 4)
# print(next_id([0,0,0,0,0,0])) #, 1)
# print(next_id([])) #, 0)



#https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6/train/python
import math
def cockroach_speed(s):
# km per hour and returns it in cm per second
#floored

# km/h to cm/s = * 27.777778
    return math.floor(s * 27.777778)




print(cockroach_speed(1.08)) #,30)
print(cockroach_speed(1.09)) #,30)
print(cockroach_speed(0)) #,0)