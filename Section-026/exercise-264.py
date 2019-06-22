class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars
        
    def __repr__(self):
        return str(self.num_cars) + " car train"
        
    def __len__(self):
        return self.num_cars

a_train = Train(4)
print(a_train)
print(len(a_train))