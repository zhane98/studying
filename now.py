def parse_float(string):
    
    # string_checker = ''.join([c for c in string if c.isdigit()]) #we would only have dave is this was True
    
    try:
        return float(string)
    
    except:
        return None 


print(parse_float("1.0")) #1.0),
print(parse_float("a")) #, None),
print(parse_float("234.0234")) #, 234.0234)

# print(type()

# print(type(x))