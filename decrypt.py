import pyfiglet

#Intro
input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" *80)

greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "bubble"))

print("\033[90m=" *80)

#Pseudocode
#ask user for input
input_str = input("\033[94mPlease enter a string to decrypt: ")
output_str = ""
#check each characters
#if '*' , change to a
for i in range(len(input_str)):
    if input_str[i] == "*":
        output_str += "a"
#if '&' , change to e
    elif input_str[i] == "&":
        output_str += "e"
#if '#' , change to i
    elif input_str[i] == "#":
        output_str += "i"
#if '+' , change to o
    elif input_str[i] == "+":
        output_str += "o"
#if '!' , change to u
    elif input_str[i] == "!":
        output_str += "u"
    else :
        output_str += input_str[i]

#print output
print("\n\033[98mYour string: ", input_str)
print("\n\033[98mThe Plain Text: ", output_str)

print("\033[90m=" *80)
#Outro
greet1 = "THANK YOU!"
print("\033[92m" + pyfiglet.figlet_format(greet1, font = "bubble"))
print("\033[90m=" *80)