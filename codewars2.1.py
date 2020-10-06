# You need to work out if the shark will get to you before you can get to the pontoon. To make it easier...

# A - sharkDistance
# distance from the shark to the pontoon. The shark will eat you if it reaches you before you escape to the pontoon.

# B - sharkSpeed
# how fast it can move in metres/second.

# C - pontoonDistance
# how far you need to swim to safety in metres.

# D - youSpeed
# how fast you can swim in metres/second.

# E - dolphin
# a boolean, if true, you can half the swimming speed of the shark as the dolphin will attack it.

#  you make it, return "Alive!", if not, return "Shark Bait!".

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    time_human = pontoon_distance / you_speed 
    
    if dolphin == True:
        shark_speed = int(shark_speed / 2)  # Quicked way = return "Alive!" if (pontoonDistance / youSpeed) < sharkDistance / (sharkSpeed - (sharkSpeed * 0.5 * dolphin)) else "Shark Bait!"
                                            # To reiterate: "sharkSpeed - (sharkSpeed * 0.5 * dolphin)" - The dolphin boolean: If true = value of 1, if fale = value of 0. Thus, if true the sharkspeed will just halve, but if false contents of parenthases will be 0 (then just subtracting 0 which doesn't alter sharkspeed (as there's no dolphin present)).
    if shark_distance != 0 and shark_speed != 0:
        time_shark = shark_distance / shark_speed
    else:
        return "Shark Bait!"

    if time_human < time_shark:
        return "Alive!"
    else:
        return "Shark Bait!"


print(shark(12, 50, 4, 8, True))
print(shark(7, 55, 4, 16, True))
print(shark(24, 0, 4, 0, True))