from datetime import date
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TripScheduling.TripValidator import TripValidator 
from TripScheduling.Passenger import Passenger 
from TripScheduling.Trip import Trip 
from TripScheduling.TimePriorityQueue import TimePriorityQueue 
from TripScheduling.driver import Driver
from TripScheduling.TripPlanner import TripPlanner

def test_addTrip():
    tp = TripPlanner()
    curr_date = date.today()
    tp.addTrip(curr_date, 7, 'Austin', 'Dallas')

    assert len(tp.trips.q) == 1

def test_offerRidePrices():
    tp = TripPlanner()
    hour = 7
    prices = tp.offerRidePrices('Austin', 'Dallas', hour)
    print(prices)
    assert len(prices) == len(range(hour, 21, 2))