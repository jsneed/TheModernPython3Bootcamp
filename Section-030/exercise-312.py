'''
Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words, and characters 
in the file.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. 
This is also the text used in the tests.)

statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(story):
    lines = 0
    with open(story, "r") as file:
        text = file.readlines()
        lines = len(text)
        file.seek(0)
        text = file.read()
        chars = len(text)
        text = text.replace('\n', ' ')
        words = len(text.split(' '))
    return {'lines': lines, 'words': words, 'characters': chars}

print(statistics('sample_text.txt'))
print(statistics('story.txt'))