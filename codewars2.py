# RETURNING STRINGS
#  Make a function that will return a greeting statement that uses an input;
# your program should return, "Hello, <name> how are you doing today?".

def greet(name):
    #Good Luck (like you need it)
    return "Hello, " + name + " how are you doing today?"


print(greet('Zhané')) #calling the function and passing the parameter 'zhané'
print(greet('Calvin'))
print(greet('Mum'))


# "Hello, Zhané how are you doing today?"


def temp(integ):
    print(f"You are {integ} years old") # f-strings let's us do String Interpolation

temp(39)




#IS n DIVISIBLE BY x and y?
def is_divisible(n,x,y):

    if n % x == 0 and n % y == 0:
        return True
    else:
        return False

is_divisible(3, 3, 4) # False
is_divisible(12, 3, 4) # True


# Calvin Solution
def is_divisible1(n,x,y):
  return n % x == 0 and n % y == 0

print(is_divisible1(3, 3, 4)) # False
print(is_divisible1(12, 3, 4)) # True

# True == True = True
# False == True = False
# False == False = False