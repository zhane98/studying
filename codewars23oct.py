# if half or more of a string in username is found in password, return false
# if half or more of a string in password is found in username, return false
# if half or less of a string in username is found in password, return true 
# if half or less of a string in password is found in username, return true 
# if username has half or more  of the length of password, false


#def validate(username, password):


    # u_length = list(username)
    # p_length = list(password)


# u_length = len("sword")
# p_length = len("password")  #False

u_length = len("")
p_length = len("password")  #False

# print(u_length)
# print(p_length)

# if u_length >= float(0.5) * int(p_length) or p_length >= float(0.5) * int(u_length):
#     print("False")
# elif u_length <= float(0.5) * int(p_length) or p_length <= float(0.5) * int(u_length):
#     print("True")
# else: 
#     print("Cannot do")


# print(validate("", "")) #, False)
# print(validate("sword", "password" )) #, False)
# print(validate("qwertyuiop", "asdfghjkl")) #, True)



#You won't allow users to have half their password repeated in their username, or half their username repeated in their password.