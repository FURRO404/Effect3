#=============FURRO404=============#
#Effect3.py
from colorama import *
from termcolor import *
import random
import time
init()
#----------------------------------#
def listconv(line):
    str1 = " "
    return (str1.join(line))

line = []
choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

while True:
    repeat = random.randint(5, 15) #Chooce how many times to repeat the number.
    space = random.randint(0, 100) #100 is maximum distance for line length.
    choice = random.choice(choices) #Choose a random symbol.
    color = random.randint(0, 1) #Get a random number for color chance.
    
    for i in range(0, repeat):
        for i in range(0, space):
            line.append(" ")
        if color == 0:
            line.append(colored(choice, 'green'))
        elif color == 1:
            line.append(colored(choice, 'red'))
        
        x = (listconv(line))
        print(colored(x))
        line.clear()
        time.sleep(0.01)
    print("\n\n")
#=============FURRO404=============#
