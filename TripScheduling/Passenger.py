class Passenger:
    def __init__(self, name):
        self.name = name

    def selectTrip(self, tripOptions):
        '''
        Given a list of trip options, a passenger may select a trip
        This trip is then added to the trip queue, which allows for later return pricing

        tripOptions: the queue of given trips available to the passenger
        This should come from TripPlanner.offerReturnPrices()

        returns the index of the desired trip
        '''

        for idx, trip in enumerate(tripOptions):
            print(f'Trip Number: {idx}\n{repr(trip)}')
        trip_num = 100
        while trip_num < 0 and trip_num > len(tripOptions):
            trip_num = int(input('enter desired trip number: '))
            
        return trip_num

    def stateSource(self):
        return input('enter desired source: ')

    def stateDestination(self):
        return input('enter desired destination: ')

    def stateHour(self):
        return int(input('enter desired hour to leave: '))