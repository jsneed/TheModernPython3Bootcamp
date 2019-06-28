'''
SOLUTION: mode
Mode Solution
This is another trickier exercise.  Don't feel bad if you were unable to complete it!

I start by defining the function, which accepts a single argument we'll call collection .

Next, I create a new dictionary that maps items in the collection to the number of times they appear in the collection. I used a dictionary comprehension along with count()  to achieve this.

count = {val: collection.count(val) for val in collection}
If collection was the string "happy", the resulting count dict would look like this:
'''
{
    'h': 1, 
    'a': 1, 
    'p': 2, 
    'y': 1
}
'''
Now, I just need to find the maximum number in all the values (2 in my example).  To do that, I use

max_value = max(count.values())
Now we know what the maximum value is, we just have to find the corresponding key. (we have 2, and need to work backwards to find 'p').  This is harder than you might think.

I convert the values in the dict to a list.  I do the same thing to all the keys.  Then, I find the index of max_value in the values and use that to access the corresponding key.

#find index of max_value in the values
correct_index = list(count.values()).index(max_value)
#use that index to find the correct key
return list(count.keys())[correct_index]
Here is the complete code:
'''

def mode(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]
