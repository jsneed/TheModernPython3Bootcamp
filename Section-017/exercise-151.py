#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    result = []
    for i in range(1, 50):
        if(i % 2 == 0):
            result.append(i)
    return result

def generate_evens():
    result = [i for i in range(1, 50) if i % 2 == 0]
    return result

print(generate_evens())
