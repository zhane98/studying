weight = input("weight: ")
unit = input("Kg or Lb ? ")
lbs = int(weight) / 2.205
kg = int(weight) * 2.205

if unit.lower() == "lb":
    print("Weight in Kg: " + str(lbs))
elif unit.lower() == "kg":
    print("Weight in Lb: " + str(kg))
else:
    print("please try again")

# print(weight)
# print(unit)
# *2.205 (kg to lb)
# /2.205 (lb to kg)
# string to integer
# print(type(weight))
# print(type(lbs))