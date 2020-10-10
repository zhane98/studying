# string formatting/interpolation = %s inside of a string to mark where we want other strings inserted.
# E.g:

name = 'Calvin'
place = 'KFC'
time = '8 pm'                    # how to add pm
food = 'chicken'
print("Hello %s, you are invited to a party at %s at %s. Please bring %s." %(name, place, time, food))