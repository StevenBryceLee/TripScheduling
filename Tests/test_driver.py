import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TripScheduling.driver import Driver

def test_addPassenger():
    '''
    Tests the addPassenger function
    '''
    driver = Driver()
    driver.addPassenger()
    driver.addPassenger()

    assert driver.passengers == 2

def test_removePassengers():
    '''
    Tests the removePassenger function
    '''
    driver = Driver()
    driver.addPassenger()
    driver.addPassenger()
    driver.removePassengers()

    assert driver.passengers == 0

def test_repr():
    '''
    Tests the repr function
    '''
    driver = Driver()
    driver.addPassenger()
    driver.addPassenger()
    driver.removePassengers()

    assert repr(driver) == 'Passengers: 0'