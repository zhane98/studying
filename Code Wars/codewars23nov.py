# #https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f/train/python

# def find_screen_height(width, ratio): 


#     x = ratio.split(":")
    
#     width2 = round(width / 0.5 ) * 0.5
#     height = (width2 / int(x[0]) * int(x[1])

    
#     # return f"{width}x{height}"

#     print(f"{width}x{height}")


# print(find_screen_height(1024, "4:3")) #, "1024x768")
# print(find_screen_height(1280, "16:9")) #, "1280x720")
# print(find_screen_height(3840, "32:9")) #, "3840x1080")




# #https://www.codewars.com/kata/568dc69683322417eb00002c

# def triple_x(s):






# print((triple_x("")) #, False)
# print((triple_x("there's no XXX here")) #, False)
# print((triple_x("abraxxxas")) #,True);
# print((triple_x("xoxotrololololololoxxx")) #,False);
# print((triple_x("soft kitty, warm kitty, xxxxx")) #,True);
# print((triple_x("softx kitty, warm kitty, xxxxx")) #,False)



#https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

def bmi(weight, height):

    bmi = weight / (height ** 2)
    

    cat = {bmi <= 18.5: "Underweight",
        bmi <= 25.0 : "Normal",
        bmi <= 30.0 : "Overweight",
        bmi > 30: "Obese"
        }

    return cat.values()





    if bmi <= 18.5:
        return "Underweight"

    elif bmi <= 25.0: 
        return "Normal"

    elif bmi <= 30.0:
        return "Overweight" 
    
    elif bmi > 30: 
        return "Obese"


print(bmi(50, 1.80)) #, "Underweight")
print(bmi(80, 1.80)) #, "Normal")
print(bmi(90, 1.80)) #, "Overweight")
print(bmi(110, 1.80)) #, "Obese")
print(bmi(50, 1.50)) #, "Normal")