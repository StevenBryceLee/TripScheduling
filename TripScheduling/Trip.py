from TripScheduling.driver import Driver

class Trip:
    def __init__(self, date, origin, destination, driver = Driver(), price = 20):
        self.date = date
        self.origin = origin
        self.destination = destination
        self.driver = driver
        self.price = price
    
    def __repr__(self):
        return f'''{self.date}, {self.origin}, 
        {self.destination}, {repr(self.driver)}, 
        ${self.price}'''