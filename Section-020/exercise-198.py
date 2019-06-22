#<p>Write a function <code>max_magnitude</code>&nbsp; that accepts a single list full of numbers.&nbsp; t should return the magnitude of the number with the largest
# magnitude(the number that is furthest away from zero).&nbsp;&nbsp;</p>
def max_magnitude(nums):
    return max([abs(n) for n in nums])
