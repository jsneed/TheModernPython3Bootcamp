import json
import requests
import pyfiglet
import termcolor
import random

dad_joke_url = "https://icanhazdadjoke.com/search"

def ascii_art(msg, color="blue", **kwargs):
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    on_colors = ['on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white']
    options = {}

    if color not in colors: color = 'cyan'
    if 'on_color' in kwargs:
        if kwargs['on_color'] not in on_colors: on_color = 'on_white'
        options['on_color'] = kwargs['on_color']

    print(color)
    print(options)
    ascii_art = pyfiglet.figlet_format(msg)
    color_ascii_art = termcolor.colored(ascii_art, color=color, **options)

    return color_ascii_art

def get_dad_jokes(msg):
    headers = {"Accept": "application/json"}
    params = {"term" : msg}
    response = requests.get(dad_joke_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        num_jokes = int(data['total_jokes'])
        if num_jokes == 0:
            print(f"Sorry, I've got 0 jokes about {msg}. Please try again.")
        elif num_jokes == 1:
            print(f"I've got one joke about {msg}. Here it is: ")
            print(data['results'][0]['joke'])
        else:
            num = random.randint(1, num_jokes)
            print(f"I've got {num_jokes} jokes about {msg}. Here's one: ")
            print(data['results'][num-1]['joke'])

#print(ascii_art("Dad Joke API App", 'blue', on_color='on_white'))
print(ascii_art("Dad Joke API App", 'blue'))
msg = input("Let me tell you a joke! Give me a topic: ")
get_dad_jokes(msg)
