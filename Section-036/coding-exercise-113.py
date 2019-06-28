'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(sentence):
    result = [i[0].upper() + i[1:] for i in sentence.split(' ')]
    s = " "
    return s.join(result)
    
    '''
    result = ""
    words = sentence.split('\s')
    for i in words:
        result += i[0].upper
    '''
    
    

print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"