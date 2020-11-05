#https://www.codewars.com/kata/5d0365accfd09600130a00c9/train/python

def solve(arr):

    # a = arr[0]    each subarray is a separate index
    # return a

    # a = sorted(arr[0])
    # return a

    # for x in range(len(arr[0:])):
    #     return sorted(arr[0:])

    a = sorted(arr[0])
    b = sorted(arr[1])
    x = a, b
    #return x

    #return a[-1] * b[-1]
    
    if abs(a[0]) > abs(a[-1]) and abs(b[0]) > abs(b[-1]):
        return a[0] * b[0] >= 0

    elif abs(a[-1]) > abs(a[0]) and abs(b[-1]) > abs(b[0]):
        return a[-1] * b[-1]
    
    elif abs(a[0]) > abs(a[-1]) and abs(b[0]) > abs(b[-1]) 



print(solve([[1, 2],[3, 4]])) #,8)
print(solve([[10,-15],[-1,-3]])) #,45)
print(solve([[-1,2,-3,4],[1,-2,3,-4]])) #,12)
print(solve([[-11,-6],[-20,-20],[18,-4],[-20, 1]])) #,17600)