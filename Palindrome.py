# Name: Nicholas Vickery
# Date: 9/11/2023
# Project: Palindrom



# Report: Ts is short for The string that I am passing through the function
# final means final string 
# userSentence is for the user's input
# palindrom is used as the functions name

import re 

def palindrom(Ts):
    # Having read over the w3 schools section of Regex, I found re.sub is a good way to check if anything is not a letter or a number
    # Sub replaces one or many matches with a string
    # r is there to indicate a raw string and tells the program the string as is
    # The ^ negates the set so it matches characters that is not lowercase, uppercase letter or a digit
    # The '' is there to remove the spaces 
    final = re.sub(r'[^a-zA-Z0-9]', '', Ts)
    # In this statement, The computer is forcing the string that has been inputed by the user to lower case letters
    final = final.lower()
    # this line is comparing the string the computer had edited to the reverse version of the string 
    # PERSONAL NOTE [::-1] puts what ever is the input in reverse 
    return final == final[::-1]

# Allows the user to input
userSentence = input("Please enter your string: ")

# runs and checks the users input to see if is a palindrom and if the user input is a palindrom then the computer will print true and if the users input is not the computer will print false
print(palindrom(userSentence))