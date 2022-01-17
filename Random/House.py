from colorama import Fore, Back, Style
width = 1
space = 9
for i in range(10):
    print (" " * space + "/" + "*" * width + "\\" + "-" * 30 + "\\")
    width += 2
    space += -1

for i in range(10):
    print ("|" + " " * 18 + " |" + " " * 30 + " |")

print("-" * 53)