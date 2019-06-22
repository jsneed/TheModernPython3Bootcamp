'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    msg = 'no'
    while True:
        if msg == 'yes':
            msg = 'no'
        elif msg == 'no':
            msg = 'yes'
        yield msg
