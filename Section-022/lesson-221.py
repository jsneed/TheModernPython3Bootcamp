import pyfiglet
import termcolor

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
msg = input("What message do you want to print? ")
color = input("What color? ")

if color not in colors:
    color = 'cyan'

ascii_art = pyfiglet.figlet_format(msg)
color_ascii_art = termcolor.colored(ascii_art, color='blue')
print(color_ascii_art)
