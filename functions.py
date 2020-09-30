import math 
                                # functions can be used multiple times throughout, with different parameters/numbers.
def get_area_of_circle(doodoo = 10):  #hasn't got a value until we pass it a parameter, which it uses temporarily for the function to run. This once run, it's tossed aside.
    return doodoo * doodoo * math.pi

radius = 4
area = get_area_of_circle(3)

print(area)

area2 = get_area_of_circle() # default parameter of 10, for e.g. can run without an argument as the default is 10.

print(area2)