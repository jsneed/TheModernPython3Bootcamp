# List Exercises 4
# Given the string <em>"amazing"</em>, create a variable called&nbsp;<strong>answer</strong>, which is a list containing all the letters from <em>"amazing"</em>
# but not the vowels (a, e, i, o, and u).&nbsp; The answer should look like: ['m', 'z', 'n', 'g'].

word = "amazing"
answer = [char for char in word if char not in ["a", "e", "i", "o", "u"]]

answer2 = [char for char in word if char not in ["aeiou"]]
