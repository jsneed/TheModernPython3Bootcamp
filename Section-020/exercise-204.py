#<p>Write a function <code>interleave</code>&nbsp; that accepts two strings.&nbsp; It should return a new string containing the 2 strings interwoven or
# zipped together. For example:</p>
# interleave('hi','ha')  # 'hhia'
# interleave('aaa', 'zzz') # 'azazaz'
# interleave('lzr','iad') #  'lizard'

def interleave(str1, str2):
    return ''.join([''.join(i) for i in zip(str1, str2)])


print(interleave('hi','ha'))
print(interleave('aaa', 'zzz'))
print(interleave('lzr','iad'))
