def is_divide_by(number, a, b):
  if (number % a == 0 and number % b == 0):
    return(True)
  else:
    return(False) # not converting True or False to strings, we're just returning the Boolean, and can only return 1 thing.
    
is_divide_by(-12, 2, -6)
is_divide_by(-12, 2, -5)

# array/list

#for i in range(3, 12):
    #print(i)

def arr(n = 0): # function with default value
    new_list = [] # Empty list to append items to later

    for num in range(n): 
        # range with 1 number will go from 0 -> n automatically
        # loop over the range and for each **num** in range 0 -> n, append it to the empty new_list
        new_list.append(num)
        
    return(new_list) 

print(arr(10))


# for n in arr(n):
#     print([0,  n - 1])



    # [ the numbers 0 to N-1 ] range, default value. Range into a list, and then into a return, as only 1 can be returned.
    # new_array = [] to create an empty list 



# any value of n, want to just return a list of 0 to n-1
# need a loop, to read that it's given 0, then continue until n-1 is reached 