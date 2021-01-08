#https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python

# def find_average(numbers):

#     add = sum(numbers)
#     length = len(numbers)

#     return add / length

# print(find_average([1, 2, 3])) #, 2) 





#https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python

# def problem(a):

    
#     if type(a) == str:
#         return "Error"
#     else:
#         return a * 50 + 6
        


# print(problem("hello")) #, "Error")
# print(problem(1)) #, 56)




#https://www.codewars.com/kata/5b853229cfde412a470000d0

# def twice_as_old(dad_years_old, son_years_old):

#     double = son_years_old * 2
    
#                                             #dad already past age 
#     if double < dad_years_old:
#         return dad_years_old - double 
#     else:
#         return double - dad_years_old


# print(twice_as_old(36,7)) # , 22)
# print(twice_as_old(55,30)) # , 5)
# print(twice_as_old(42,21)) # , 0)
# print(twice_as_old(22,1)) # , 20)
# print(twice_as_old(29,0)) # , 29)




#https://www.codewars.com/kata/568d0dd208ee69389d000016

# def rental_car_cost(d):

#     if d < 3:
#         return d * 40
#     elif 3 <= d < 7:
#         return d * 40 - 20
#     elif d >= 7:
#         return d * 40 - 50



# print(rental_car_cost(1)) #,40)
# print(rental_car_cost(4)) #,140)
# print(rental_car_cost(7)) #,230)
# print(rental_car_cost(8)) #,270)



#https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

def lovefunc( flower1, flower2):

    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    else:
        return False
    

print(lovefunc(1,4)) #, True)
print(lovefunc(2,2)) #, False)
print(lovefunc(0,1)) #, True)
print(lovefunc(0,0)) #, False)

# function lovefunc(flower1, flower2) {
#   let one;
#   let two;
#   if (flower1 % 2 === 0) one = true;
#   if (flower2 % 2 === 0) two = true;
#   return one !== two;
# }