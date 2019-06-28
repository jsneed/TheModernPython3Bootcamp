'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''
# Dictionary Comprehension
def vowel_count(word):
    vowels = "aeiou"
    return {x : word.lower().count(x) for x in vowels if word.lower().count(x) > 0}

print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie')) # {'e': 2, 'i': 1}
print(vowel_count('Colt')) # {'o': 1}
