# #https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
# def points(games):

#     points = 0

#     for score in games:

#         x = score[0]
#         y = score[2]

#         if x > y:
#             points += 3
#         elif x < y:
#             None
#         elif x == y:
#             points += 1 

#     return points



# print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])) #, 30)
# print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'])) #, 10)
# print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4'])) #, 0)
# print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'])) #, 15)
# print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4'])) #, 12)




#https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
# def abbrev_name(name):

#     spl = name.split()
  
#     first = spl[0][0]
#     last = spl[1][0]
    
#     initials = first + "." + last
#     return initials.upper()


# print(abbrev_name("Sam Harris")) #, "S.H");
# print(abbrev_name("Evan Cole")) #, "E.C");
# print(abbrev_name("David Mendieta")) #, "D.M");





#https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
# def paperwork(n, m):

#     return n * m if n > 0 and m > 0 else 0

# print(paperwork(5,5)) #, 25, "Failed at Paperwork(5,5)")




#https://www.codewars.com/kata/5715eaedb436cf5606000381
# def positive_sum(arr = 0):

#     #[i for i in arr] - give you back the same list 

#     list_comprehension = sum([i for i in arr if i > 0])
#     return list_comprehension 


# print(positive_sum([1,2,3,4,5])) #,15)
# print(positive_sum([1,-2,3,4,5])) #,13)
# print(positive_sum([-1,2,3,4,-5])) #,9)
