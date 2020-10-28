# https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python

# def set_alarm(employed, vacation):

#     if employed == True and vacation == False:
#         return True
#     else: 
#         return False


# print(set_alarm(True, True)) #-> False
# print(set_alarm(False, True)) #-> False
# print(set_alarm(False, False)) #-> False
# print(set_alarm(True, False)) #-> true

# https://www.codewars.com/kata/57d814e4950d8489720008db/train/python

# def index(array, n):
    
#     try:
#         return array[n] ** n

#     except:
#         return -1
    

# print(index([1, 2, 3, 4],7)) #,9)
# print(index([1, 3, 10, 100],3)) #,1000000)


# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python

# def past(h, m, s):          #milliseconds -> 1,000 ms = 1 second

#    # 1000 ms = 1 s
#    # 60000 ms = 1 m
#    # 3,600,000 ms = 1 h

#    return (h * 3600000) + (m * 60000) + (s * 1000)

# print((past(0,1,1))) #,61000)
# print((past(1,1,1))) #,3661000)
# print((past(0,0,0))) #,0)






# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def areYouPlayingBanjo(name):
    
    if name.startswith(" R" or " r"):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# calvin = return f"{name} plays" if name[0].lower() == "r" else f"{name} no play"


print(areYouPlayingBanjo("martin")) #, "martin does not play banjo");
print(areYouPlayingBanjo("Rikke")) #, "Rikke plays banjo");