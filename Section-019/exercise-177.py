# Two star args **kwargs returnd all remainging arguments as a key word dictionary

# Define combine_words below:
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    else:
        return word

print(combine_words("child"))
print(combine_words("child", prefix="man"))
