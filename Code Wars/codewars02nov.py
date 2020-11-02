#https://www.codewars.com/kata/56dae9dc54c0acd29d00109a/train/python
# def main(verb, noun):
#     return verb + noun


#https://www.codewars.com/kata/5625618b1fe21ab49f00001f/train/python
# def say_hello(name):
#     return f"Hello, {name}"

#https://www.codewars.com/kata/595970246c9b8fa0a8000086/train/python
#def capitalize_word(word):
    #return word.title()
    #return "".join(char.upper() for char in word[0])

#https://www.codewars.com/kata/55cb854deb36f11f130000e1/train/python
# def weather_info(temp):
#     c = convert_to_celsius(temp)
#     if (c < 0):
#         return (str(c) + " is freezing temperature")
#     else:
#         return (str(c) + " is above freezing temperature")
    
# def convert_to_celsius(temperature):
#     var_celsius = (temperature - 32) * (5/9)
#     return var_celsius

#https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python

# def area_or_perimeter(l , w):
#     return l * w if l == w else (l * 2) + (w * 2)
    
#     # if l == w:
#     #     return l * w
#     # else:
#     #     return (l * 2) + (w * 2)

# print(area_or_perimeter(4, 4)) #, 16)
# print(area_or_perimeter(6, 10)) #, 32)


#https://www.codewars.com/kata/55ca77fa094a2af31f00002a
# la_liga_goals = 43
# champions_league_goals = 10
# copa_del_rey_goals = 5

# total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


#https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
# def repeat_str(repeat, string):
#     return string * repeat


# print(repeat_str(4, 'a')) #, 'aaaa')
# print(repeat_str(3, 'hello ')) #, 'hello hello hello ')
# print(repeat_str(2, 'abc')) #, 'abcabc')

#https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
def fake_bin(x):
    
    #new_list = list(x)
    empty_string = ""           #depending on what the end result need to be
    
    for num in x:
        if int(num) < 5:
            empty_string += "0"            #+= concatenation for strings, + is a calculation            
        else:
            empty_string += "1"
    return empty_string

print(fake_bin("45385593107843568"))

# for num in convert:
#         if num < 5:
#             return str(0)
#         else:
#             return str(1)
