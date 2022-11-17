# Hint: You will want to use a classic LinkedList Node to implement the tour.
class Node:
    def __init__(self, point: 'Point'):
        # This node's point
        self.point = point
        # The next node
        self.next = None

# (2D point data type to model points in the plane.)
class Point:
    # create the point (x, y)
    def __init__(self, x: float, y: float):
        pass

    # Returns a string representation of the point.
    # Should be in coordinate pair output. I.e. (x, y)
    def __str__(self) -> str:
        pass

    # return Euclidean distance between the two points
    def distance_to(self, that: 'Point') -> float:
        pass

'''
Tour class which is a collection of ordered points.
The functions allow you to insert points in a way that will 
keep the distance of the tour as small as possible.

Each Tour object should be able to print out the points in order, 
count its number of points, compute its total distance, 
and insert a new point using either of the two heuristics. 
The constructor creates an empty tour.
'''

class Tour:
    # Creates an empty tour
    # Initialize any instance variables you think are needed.
    def __init__(self):
        pass

    # Returns string representation of the Tour.
    # Should output a list of all points on the Tour.
    def __str__(self) -> str:
        pass

    # return the number of points on tour
    # Hint: You should not have to iterate through the entire Tour to get the size.
    def size(self) -> int:
        pass

    # Computers and returns the distance of entire tour
    def distance(self) -> float:
        pass

    # Helper function to insert a new point p into the Tour after a previous point prev.
    # Example if the tour is a -> b -> c -> d
    # And you call _insert_at(p, c). Then the Tour should look like.
    # a -> b -> c -> p -> d
    # You can use this helper function in the insert_nearest and insert_smallest
    # once you find the point you should insert p after.
    def _insert_at(self, p: 'Point', prev: 'Node') -> None:
        pass

    # Insert a new Point p to the Tour using neearest neighbor heuristic
    def insert_nearest(self, p: 'Point') -> None:
        pass

    # Insert a new Point p to the Tour using smallest increase heuristic
    def insert_smallest(self, p: 'Point') -> None:
        pass
