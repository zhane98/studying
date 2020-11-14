# #https://www.codewars.com/kata/57cc40b2f8392dbf2a0003ce/train/python

# def check(a, x): 
    
#     new = []
    
#     second = new.append(a).lower()
#     print(second)

# print(check([80, 117, 115, 104, 45, 85, 112, 115], 45)) #, True)
# print(check(['t', 'e', 's', 't'], 'e')) #, True)


#  if x in a:
#         return True
#     else:
#         return False






#https://www.codewars.com/kata/5a145ab08ba9148dd6000094/train/python
import pdb


# append is to conca. lists, += is to conca. string, later convert


def doubles(text):
    empty_list = []
    
    for letter in text:
        
        if empty_list and empty_list[-1] == letter:
            empty_list.pop()

        else:
            empty_list.append(letter)
            
    return ''.join(empty_list)


print(doubles('abbbzz')) #,'ab'
print(doubles('ykkkd')) #,'ykd'
print(doubles('abbcccdddda')) #,'aca'
print(doubles('vvvvvoiiiiin')) #,'voin'
print(doubles('rrrmooomqqqqj')) #,'rmomj'
print(doubles('xxbnnnnnyaaaaam')) #,'bnyam')