'''
Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file to the second file. 

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. 
This is also the text used in the tests.

copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(story_file, copy_file):
    s_file = open(story_file, "r")
    w_file = open(copy_file, "a")
    lines = s_file.readlines()
    for line in lines:
        w_file.write(line)
    s_file.close()
    w_file.close()
