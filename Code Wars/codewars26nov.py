#ashttps://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

# def reverseWords(s):

#     apart = s.split(" ")
#     opp = apart[::-1]
#     final = ' '.join(opp)
#     return final


# print(reverseWords("hello world!")) #, "world! hello")



#https://www.codewars.com/kata/59d0ee709f0cbcf65400003b/train/python

states = {'AZ': 'Arizona',
'CA': 'California',
'ID': 'Idaho',
'IN': 'Indiana',
'MA': 'Massachusetts',
'OK': 'Oklahoma',
'PA': 'Pennsylvania',
'VA': 'Virginia'
}


def by_state(str):
    list_of_peeps = str.split("\n") #8 strings
    
    #address_book = []

    for person in list_of_peeps:
        # print(person.split()[-1])
        
        temp_dict = {}
        
        state_code = person[-2:]
        state_name = states[state_code]

        temp_dict[state_name] = person.replace(state_code, state_name)
        # [{'Massachusetts': 'Dave Daggett, 341 King Road, Plymouth Massachusetts'}]
        
        #address_book.append(temp_dict)

    
    # for line in temp_dict:
    #     print(line)

    


case1 = """Dave Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Orville Thomas, 11345 Oak Bridge Road, Tulsa OK
Terry Kalkas, 402 Lans Road, Beaver Falls PA
Eric Adams, 20 Post Road, Sudbury MA
Hubert Sims, 328A Brook Road, Roanoke MA
Amy Wilde, 334 Bayshore Pkwy, Mountain View CA
Sal Carpenter, 73 6th Street, Boston MA"""

print(by_state(case1))

# California\r\n
# .....Amy Wilde 334 Bayshore Pkwy Mountain View California\r\n

# Massachusetts\r\n
# ..... Eric Adams 20 Post Road Sudbury Massachusetts\r\n
# ..... Hubert Sims 328A Brook Road Roanoke Massachusetts\r\n
# ..... John Daggett 341 King Road Plymouth Massachusetts\r\n
# ..... Sal Carpenter 73 6th Street Boston Massachusetts\r\n

# Oklahoma\r\n
# ..... Orville Thomas 11345 Oak Bridge Road Tulsa Oklahoma\r\n

# Pennsylvania\r\n
# ..... Terry Kalkas 402 Lans Road Beaver Falls

# Pennsylvania\r\n Virginia\r\n
# ..... Alice Ford 22 East Broadway Richmond Virginia