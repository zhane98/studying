def sakura_fall(v):

    #Distance = Speed * Time         # (cm) = (cm/s) * (s)
    #Distance = 5 * 80 = 400 cm
    Distance = 400                  
    
    # from the same branch, so same distance 
    # given a speed and have to calculate time
    #Time = Distance(400) / Speed(given)

    if v >= 1:
        return Distance / v 
    elif v == 0:
        return 0
    else:
        return 0



# falling speed of a petal is 5 centimeters per second (5 cm/s)
# 80 seconds for the petal to reach the ground from a certain branch.

print(sakura_fall(5)) #, 80)
print(sakura_fall(10)) #, 40)
print(sakura_fall(-1)) #, 0)