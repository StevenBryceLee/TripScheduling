from datetime import date, timedelta
import pandas as pd

from .Trip import Trip
from .TimePriorityQueue import TimePriorityQueue

class TripValidator:
    def __init__(self):
        return
    
    def isReturn(self, source, destination, trip_queue):
        '''
        This function checks to see if a trip would be a return trip

        This is determined by whether or not there was a trip which targeted
        the source city in the past and would therefore be eligible for return
        pricing

        source is the source city from which the requested trip will leave
        destination is the destination city to which the trip will go

        returns True if there is a currently available trip with the same
        source, same destination, and an available driver
        '''
        # No trips scheduled, so this trip will not be a return trip
        if not trip_queue:
            return False
        
        # Count the number of drivers who should be in the city
        drivers_in_city = 0 

        for trip in trip_queue.q:
            if (trip.origin == source and
                trip.destination == destination and
                trip.driver.passengers < 3):
                return True
    
    def validateTrip(self, date, hour):
        '''
        This function performs data validation on a requested trip
        
        date: This must be a timestamp of the form yyyy-mm-dd
        hour: This must be an integer >= 7 and <= 19
        
        returns: timestamp of date with hour
        '''

        if type(hour) is not int:
            raise TypeError("hour is not an integer")
        if hour < 7 or hour > 19:
            raise ValueError("hour is outside of normal travel times")
        converted_date = date + pd.to_timedelta(hour, unit='h')
        return converted_date
    