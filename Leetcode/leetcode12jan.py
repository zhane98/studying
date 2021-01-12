# class Solution(object):
#     def reverse(self, x):
#         if x == '':
#             return 0

#         rev = [str(b) for b in str(x)]
#         dave = rev[::-1]    
#         bat = ''.join(dave)

#         print(dave[0])

#         if dave[0] == '0' and len(dave) > 1:
#             dave.pop(0)
#             simon = ''.join(dave)
        
#             return simon

#         if x < 0:
#             dave.pop(-1)
#             neil = ''.join(dave)

#             return -int(neil)

#         return bat
 
    

#     SOLUTION:
#     def reverse(self, x):
#     s = str(x)
#     res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1])
#     return res if -2147483648 <= res <= 2147483647 else 0

# CLEANER SOLUTION
# def reverse(self, x):
#     if x>=0:
#         res = int(str(x)[::-1])
#     else:
#         res = int('-' + str(x)[:0:-1])



# problem = Solution()
# print(problem.reverse(982))
# print(problem.reverse(-123))
# print(problem.reverse(120))
# print(problem.reverse(0))
        

#SET UP
# def reverse(x):
#     return x 

# print(reverse(982))




#https://www.codewars.com/kata/542ebbdb494db239f8000046/train/python

def next_item(mylist, item):

    for a in mylist:
        

  





print(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5)) #, 6)
print(next_item(['a', 'b', 'c'], 'd')) #, None)
print(next_item('testing', 't')) #, 'e')
print(next_item(['a', 'b', 'c'], 'c')) #, None)





#   if item in mylist:
#         dave = mylist.index(item)
#         mike = int(dave) + 1
#         return mylist[mike]

#     else: 
#         return None
