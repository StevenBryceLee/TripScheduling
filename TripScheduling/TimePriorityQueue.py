class TimePriorityQueue:
    '''
    This class is a priority queue based on the trip class.

    Note, it is sorting based on the date attribute of each element in the queue
    This will only work based on the Trip class currently, but could be modified
    '''
    def __init__(self):
        self.q = []

    def insert(self, new_element):
        '''
        Inserts a new element in the priority queue based on the date

        new_element: an element of class Trip
        '''

        if not self.q:
            self.q.append(new_element)

        for idx, q_element in enumerate(self.q):
            if new_element.date > q_element.date:
                self.q.insert(idx, new_element)
                break

    def getQueue(self):
        return [repr(trip) for trip in self.q]