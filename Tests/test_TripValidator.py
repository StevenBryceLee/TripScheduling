from datetime import date
import os
import sys
import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TripScheduling.Trip import  Trip
from TripScheduling.TripValidator import TripValidator
from TripScheduling.TimePriorityQueue import TimePriorityQueue
from TripScheduling.driver import Driver

def test_isReturn():
    tv = TripValidator()
    source = 'Austin'
    destination = 'Dallas'
    trip_queue = TimePriorityQueue()
    curr_date = date.today()
    trip = Trip(curr_date, source, destination) 
    trip_queue.insert(trip)
    assert tv.isReturn(source, destination, trip_queue) == True

def test_validateTrip():
    tv = TripValidator()
    curr_date = date.today()
    curr_timestamp = pd.to_datetime(date.today())
    curr_hour = pd.to_datetime(date.today()).hour
    with pytest.raises(ValueError):
        tv.validateTrip(curr_date, curr_hour)