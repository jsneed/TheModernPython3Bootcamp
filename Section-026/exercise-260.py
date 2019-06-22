# Define your classes below:
class Mother:
    def __init__(self, eye_color="brown", hair_color="dark brown", hair_type="curly"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type
    
class Father:
    def __init__(self, eye_color="blue", hair_color="blond", hair_type="straight"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type
    
class Child(Mother, Father):
    def __init__(self):
        super().__init__()

child = Child()
print(child.eye_color)
print(child.hair_color)
print(child.hair_type)