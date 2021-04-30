class Driver:
    def __init__(self):
        self.passengers = 0

    def addPassenger(self):
        if self.passengers <= 3:
            self.passengers += 1

    def removePassengers(self):
        self.passengers = 0

    def __repr__(self):
        return f'Passengers: {self.passengers}'