# One star args *args returnd all remainging arguments as a tuple
def contains_purple(*args):
    if "purple" in args:
        return True
    return False
