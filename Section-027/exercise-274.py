'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(num=99, beverage='soda'):
    msg = ""
    while num >= 0:
        if num == 0:
            msg = f'No more {beverage}!'
        elif num == 1:
            msg = f'Only 1 bottle of {beverage} left!'
        else:
            msg = f'{num} bottles of {beverage} on the wall.'
        yield msg
        num -= 1
    

song = make_song(5, "beer")
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))