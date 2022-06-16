from termcolor import colored
from pyfiglet import figlet_format

txt = colored("Some information", "red")

print(txt)

txt = figlet_format(text=txt, font="isometric1")

print(txt)