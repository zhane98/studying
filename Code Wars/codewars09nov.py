#https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python

# def is_uppercase(inp):
#     return True if inp == inp.upper() else False

# print(is_uppercase("c")) #, False)
# print(is_uppercase("C")) #, True)
# print(is_uppercase("hello I AM DONALD")) #, False)
# print(is_uppercase("HELLO I AM DONALD")) #, True)



#https://www.codewars.com/kata/57ab2d6072292dbf7c000039/train/python

def correct_polish_letters(st):


    conversion = {  "ą" : "a", 
                    "ć" : "c",
                    "ę" : "e",
                    "ł" : "l",
                    "ń" : "n",
                    "ó" : "o",
                    "ś" : "s",
                    "ź" : "z",
                    "ż" : "z",
                    }

    empty = ""

    for x in st:
        if conversion.get(x, False):
          empty += conversion[x]
        else:
          empty += x
    
    return empty



def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))

return st.replace('ą','a').replace('ć','c').replace('ę','e')


print(correct_polish_letters("Jędrzej Błądziński")) #,"Jedrzej Bladzinski");
print(correct_polish_letters("Lech Wałęsa")) #,"Lech Walesa");
print(correct_polish_letters("Maria Skłodowska-Curie")) #,"Maria Sklodowska-Curie")