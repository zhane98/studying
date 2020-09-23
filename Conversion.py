weight = input("weight: ") #variable for the input of weight
unit = input("Kg or Lb ? ") # variable for the input of units
lbs = int(weight) / 2.205 # variable, converting weight string to integer (so all numbers)
kg = int(weight) * 2.205 # variable, converting weight string to integer (so all numbers)

if unit.lower() == "lb": # if statement, converting any input into lowercase, doubling checking it's equal to lb - all converted to lowercase so checking against lowercase too.
    print("Weight in Kg: " + str(lbs)) #converting the variable back into a string (from an integer)
elif unit.lower() == "kg":
    print("Weight in Lb: " + str(kg))
else:
    print("please try again") # a catch for errors (all other inputs)

# print(type(weight)) - just checking variable type
# print(type(lbs)) - just checking variable type