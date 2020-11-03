# https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python

# look up how to identify consecutive integers in an array
# length of array to do for loop (for loop searching for the consecutive integers)

#DONE loop over the array (be able to print out numbers in the array)
#DONE range/len/arr - to find length of array
#DONE print 2 numbers together, i.e. 5 and 7?? - to later check for 2 C numbers
#variable that is a and b together, and check against that- sliding window
# is 5,3 that same as a,b? etc.

# Return True is a, b are consecutive in the list

def consecutive(arr, a, b):

    test1 = a, b
    test2 = b, a

    for x in range(len(arr)-1):         #counter eachother
        window = arr[x], arr[x + 1]

        if window == test1:        #can't shorten
            return True 
            
        elif window == test2:
            return True 

    return False
   

print(consecutive([1, 3, 5, 7], 3, 7)) # False
print(consecutive([1, 3, 5, 7], 3, 1)) # True


#Smart answer = return abs(arr.index(a)-arr.index(b)) == 1



# CALVIN:
# def consecutive(arr, a, b):

#     for i in range(len(arr)-1):
#         if [a, b] == [arr[i], arr[i+1]]:
#             return True
#         elif [b, a] == [arr[i], arr[i+1]]:
#             return True

#     return False