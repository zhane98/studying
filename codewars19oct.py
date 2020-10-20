def flip(direction, sequence):

    if direction == 'R':
        sequence.sort()

    else:
        sequence.sort()
        sequence.reverse()              #sequence = sequence[::-1] called slicing.
        

    return sequence



# flip('R', [3, 2, 1, 2])     =>  [1, 2, 2, 3]
# flip('L', [1, 4, 5, 3, 5])  =>  [5, 5, 4, 3, 1]

# print(flip('R', [3, 2, 1, 2]))
# print(flip('L', [3, 2, 1, 2]))
 #[1, 2, 2, 3])


# split the string into characters 
# loop through new list. 
# for each item - figure out if it's an integer
# if it's an integer, append to a new empty list
# you will have a list with 5, 6 - use the join method to combine into 1 number. 

def get_number_from_string(string):
    
    # new_list = list(string)
    # range_of_integers = "0123456789"
    # empty_list = []


    # for character in new_list:                       # loop, then if, then append
    #     if character in range_of_integers:
    #         empty_list.append(character)
    
    # result = ''.join(empty_list)
    # return int(result)

    return int(''.join(character for character in string if character.isdigit()))
               

    # no_integers = [x for x in mylist if not isinstance(x, int)]
    # no_integers = character in string if not isinstance(character, int)

    # for characters in new_list:
    #     new_list.pop(int)
    

# remove items specifed to int - not equals int, then remove.

# ''.join(x)

print(get_number_from_string("$100 000 000")) #100000000))
print(get_number_from_string("hell5o wor6ld")) #, 56))

#  s = "foobar"
# >>> list(s)
# ['f', 'o', 'o', 'b', 'a', 'r']