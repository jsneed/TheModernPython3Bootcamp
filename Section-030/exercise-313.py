'''
Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. Replaces all instances 
of the word in the file with the replacement word.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. 
This is also the text used in the tests.)

find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file_name, word, replacement):
    with open(file_name, 'r+') as file:
        text = file.read()
        '''
        i = text.find(word, 0)
        if i != -1:
            while(i < len(text)):
                file.seek(i)
                file.write(replacement)
                i = text.find(word, i)
        '''
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()