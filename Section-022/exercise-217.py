import keyword

def contains_keyword(*args):
    for i in args:
        if keyword.iskeyword(i):
            return True
    return False


print(contains_keyword("if"))
print(contains_keyword("else", "jess", "dsfdsff"))
print(contains_keyword("fdsfsf", "fdfdsfs", "f"))
print(contains_keyword("for", "four", "if"))
print(contains_keyword("return"))
print(contains_keyword("try"))
