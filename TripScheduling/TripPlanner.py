from datetime import date
import pandas as pd

from .TripValidator import TripValidator
from .Passenger import Passenger
from .Trip import Trip
from .TimePriorityQueue import TimePriorityQueue
from .driver import Driver

class TripPlanner:
    def __init__(self):
        self.trips = TimePriorityQueue()
        self.outgoing_price = 20 # TODO placeholder for unknown supply and demand graph
        self.return_price = 10
        self.validator = TripValidator()
        self.PassengerList = []

    def addTrip(self, date, hour, source, destination):
        '''
        This function adds a trip to uncompleted trips
        
        date: This must be a timestamp of the form yyyy-mm-dd
        hour: This must be an integer >= 7 and <= 19

        returns nothing, and has a side effect of appending the trip to 
        self.trips
        '''
        valid_time = self.validator.validateTrip(date, hour)
        isReturn = self.validator.isReturn(source, destination, self.trips)
        if isReturn:
            price = self.return_price
        else:
            price = self.outgoing_price
        driver = Driver()
        driver.addPassenger()
        newTrip = Trip(valid_time, source, destination, driver, price)
        
        self.trips.insert(newTrip)

    def offerRidePrices(self, source, destination, hour):
        '''
        This function finds potential return times based on currently available trips
        
        If a spot has already been taken as an outgoing trip, then that spot 
        will not be offered at return pricing

        If a spot has not been taken as a return trip, then return pricing is 
        offered

        For all other valid spots, outgoing trip pricing is offered

        This pricing scheme incentivizes riders to select return trips if 
        possible, but allows them to pay more for outgoing trips

        source: the city from which the ride will leave
        destination: the city to which the ride will go
        hour: the current hour

        returns a list of potential trips and return prices
        '''

        trips = self.trips
        outgoing_price = self.outgoing_price
        return_price = self.return_price
     
        first_trip = self.getNextTrip(hour)        

        potential_trips = range(first_trip, 21, 2)

        # No rides are scheduled so all rides are outgoing rides
        curr_date = pd.to_datetime(date.today())
        if not trips.q:
            return_trips = [Trip(curr_date + pd.to_timedelta(hour, unit='h'), 
                            source, destination, Driver(), outgoing_price) 
                        for hour in potential_trips]
            return return_trips
        
        return_trips = []

        # For each available ride in the 2 hour segments, find ride status
        q = trips.q
        idx = 0
        for trip_hour in potential_trips:
            if idx >= len(q):
                return_trips += [Trip(curr_date + pd.to_timedelta(hour, unit='h'),
                                source, destination, Driver(), outgoing_price)]
                return return_trips

            if q[idx].driver.passengers > 3:
                idx += 1
            new_trip = trip_hour != q[idx].date.hour
            # Case: offer a trip earlier than the next scheduled trip
            if new_trip:
                return_trips.append(Trip(curr_date + pd.to_timedelta(hour, unit='h'), 
                                    source, destination, Driver(), outgoing_price))
            
            # Case: offer a currently available trip
            else:
                return_trips.append(q[idx])
                idx += 1
            
        return return_trips

    def getNextTrip(self, hour):
        '''
        This function returns the next available trip by rounding the hour up
        to the next nearest 2 hour increment starting at 7AM and ending at 7PM

        hour: an integer less than 19, representing 7PM in military time

        returns an integer representing the next nearest trip
        '''

        if hour > 19 or hour < 0:
            raise ValueError('Hour must be less than 19 and greater than 0')

        if hour < 7: 
            return 7

        remainder = hour % 2
        if remainder == 0:
            return hour

        return hour + 2 - remainder

    def addPassenger(self, name):
        '''
        Adds a passenger to the list of passengers
        '''

        self.PassengerList.append(Passenger(name))

    def getPassengerInput(self, passenger):
        '''
        Offers passengers a list of available trips, then adds their
        selected trip to the queue

        passenger: An instantiation of the Passenger class
        '''

        source = passenger.stateSource()
        dest = passenger.stateDestination()
        hour = passenger.stateHour()

        ridePrices = self.offerRidePrices(self, source, destination, hour)

        desiredRide = passenger.selectTrip(ridePrices)
        # 
        try:
            idx = self.trips.index(ridePrices[desiredRide])
            self.trips[idx].driver.addPassenger()

        except ValueError:
            self.trips.addTrip(self, pd.to_datetime(date.today()), 
                                hour, source, destination)