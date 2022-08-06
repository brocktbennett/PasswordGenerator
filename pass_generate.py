#Generate password which is tought to break. 12-15 characters is prefered. 
#import 
import random

#Give the password restrictions, comment out symbols if not needed. 
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%^&*/\?"

#creating the printed password to use. Change length if needed shorter or longer.
use_for = lower_case + upper_case + number + symbols
length_for_pass = 12

password = "".join(random.sample(use_for, length_for_pass))

#Print out the password generator result 
print("Your generated password is: "+(password))


