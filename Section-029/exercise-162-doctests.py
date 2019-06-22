'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(num):
    """
    >>> return_day(2)
    'Monday'
    """

    days = {
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
        7 : "Saturday"
    }
    return days.get(num)

print(return_day(1))
print(return_day(7))
print(return_day(41))

# To run doctest use line below:
# python -m doctest -v exercise-162-doctests.py 