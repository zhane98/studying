zhane = {
    "height": 166,
    "weight": 130,
    "age": 29,
    "city": "Liverpool",
    "country": "England"
}

print(zhane)

print(zhane["city"])

zhane["gender"] = "female" # if did gender again it will just update it to the new pair (as gender already exists)

print(zhane)

for i in zhane:
    value = zhane[i] # first loop, zhane["height"], then second loop will be zhane["weight"] and so on. 
    print("Key: " + i + " Value: " + str(value)) # now printing instead of writing dictionary, so can't print integers - have to convert it to a string.

#alternatively:
for left, right in zhane.items(): # recognises zhane as a dictionary, then 1st thing mentioned is on the left and the 2nd is on the right, so can use any word.
    print("Key: " + left + " Value: " + str(right))

print("age" in zhane) #checking if key exists
print("birthday" in zhane)

