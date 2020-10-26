# def array_plus_array(arr1,arr2):

    
#     list1 = sum(arr1)
#     list2 = sum(arr2)
    
#     return list1 + list2



# print(array_plus_array([1, 2, 3], [4, 5, 6])) # 21)
# print(array_plus_array([-1, -2, -3], [-4, -5, -6])) #, -21)
# print(array_plus_array([0, 0, 0], [4, 5, 6])) #, 15)
# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python 



#https://www.codewars.com/kata/595970246c9b8fa0a8000086/train/python


# def capitalize_word(word):
#     return "".join(char.upper() for char in word)

def capitalize_word(word):
    #return "".join(char[0].upper() + word[1:] for char in word.split())

    return word[0].upper() + word[1:]
    



print(capitalize_word('word')) #, 'Word');
print(capitalize_word('i')) #, 'I')) #;
print(capitalize_word('glasswear')) #, 'Glasswear