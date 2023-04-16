import pyfiglet

#Intro
input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" *80)

greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "bubble"))

print("\033[90m=" *80)

#Pseudocode
#ask user for input
#check each characters
#if '*' , change to a
#if '&' , change to e
#if '#' , change to i
#if '+' , change to o
#if '!' , change to u
#print output