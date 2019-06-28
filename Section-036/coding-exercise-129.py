'''
Write a function called reverse_vowels. This function should reverse the vowels in a string. Any characters which are not vowels should 
remain in their original position. You should not consider "y" to be a vowel.

reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

def reverse_vowels(msg):
    vowels = 'aeiouAEIOU'
    vowel_indexes = []
    for i, cha in enumerate(msg):
        if cha in vowels:
            vowel_indexes.append(i)

    i = 0
    count = len(vowel_indexes) - 1
    msg_list = list(msg)
    while i < len(vowel_indexes)/2:
        temp = msg_list[vowel_indexes[count]]
        msg_list[vowel_indexes[count]] = msg_list[vowel_indexes[i]]
        msg_list[vowel_indexes[i]] = temp
        count -= 1
        i += 1
        
    return "".join(msg_list)



print(reverse_vowels("Hello!")) # "Holle!" 
print(reverse_vowels("Tomatoes")) # "Temotaos" 
print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
print(reverse_vowels("aeiou")) # "uoiea"
print(reverse_vowels("why try, shy fly?")) # "why try, shy fly?"
