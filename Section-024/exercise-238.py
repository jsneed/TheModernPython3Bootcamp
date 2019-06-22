# Define the Comment class below:
class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

c = Comment('mikey', 'blah', 44)
print(c.username)
print(c.text)
print(c.likes)
