import pyfiglet

#Intro
input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" *80)

greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "bubble"))

print("\033[90m=" *80)