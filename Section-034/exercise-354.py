'''
Define a function called censor that accepts a single string. Rather than censoring any real profanity, we're going to censor any 
words that start with "frack".  This includes "fracking", "fracker", "frack", etc.  Replace the entire word with the string "CENSORED".  
Your regex should be case insensitive. For example:

censor("Frack you")                 #"CENSORED you"
censor("I hope you fracking die")   #"I hope you CENSORED die"
censor("you fracking Frack")        #"You CENSORED CENSORED"

'''
import re 

def censor(msg):
    frack_re = re.compile(r'\b(frack\w*)\b', re.IGNORECASE)
    return frack_re.sub("CENSORED", msg)

print(censor("Frack you"))                 #"CENSORED you"
print(censor("I hope you fracking die"))   #"I hope you CENSORED die"
print(censor("you fracking Frack"))        #"You CENSORED CENSORED"
