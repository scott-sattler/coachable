from point import *
from math import inf


# Hint: You will want to use a classic LinkedList Node to implement the tour.
class Node:
    def __init__(self, point: 'Point' = None):
        # This node's point
        self.point = point
        # The next node
        self.next = None
        self.next_dist = None


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
    def __init__(self, first_node: Node = Node(None)):
        self.length = 0
        if first_node is not None:
            self.length += 1
        self.head = first_node

    # Returns string representation of the Tour.
    # Should output a list of all points on the Tour.
    def __str__(self) -> str:
        # return f"{[point.position for point in self.tour]}"  was using list vs linked list
        all_points = []
        head = self.head
        while head is not None:
            all_points.append(head.point.position)
            head = head.next
        return str(all_points)

    # return the number of points on tour
    # Hint: You should not have to iterate through the entire Tour to get the size.
    # TODO: 2 approaches:
    # 1: make the first node a length node
    # 2: modify the Node class
    # 3: other?
    def size(self) -> int:
        # return len(self.tour)
        return self.length

    # Computes and returns the distance of entire tour
    def distance(self) -> float:
        distance = 0
        head = self.head
        while head.next is not None:
            distance += head.point.distance_to(head.next.point)
            head = head.next
        return distance

    # Helper function to insert a new point p into the Tour after a previous point prev.
    # Example if the tour is a -> b -> c -> d
    # And you call _insert_at(p, c). Then the Tour should look like.
    # a -> b -> c -> p -> d
    # You can use this helper function in the insert_nearest and insert_smallest
    # once you find the point you should insert p after.
    def _insert_at(self, p: 'Point', prev: 'Node') -> None:  # this should be _insert_after
        head = self.head
        while head is not prev:
            head = head.next
        new_node = Node(p)  # create new node
        new_node.next = prev.next  # link new node to next node
        prev.next = new_node  # link previous node to new node
        self.length += 1

    # Insert a new Point p to the Tour using nearest neighbor heuristic
    def insert_nearest(self, p: 'Point') -> None:
        if self.length < 1:
            self.head = Node(p)
            return None

        # look at each object, record distance
        head = self.head
        min_node = head
        min_dist = inf
        while head is not None:
            curr_dist = head.point.distance_to(p)
            if curr_dist < min_dist:
                min_node = head
                min_dist = curr_dist
            head = head.next
        self._insert_at(p, min_node)

    # Insert a new Point p to the Tour using the smallest increase heuristic
    def insert_smallest(self, p: 'Point') -> None:
        # traverse ll
        # from total distance
        #   subtract current to next node
        #   add current to new, and new to next
        # compare (minimize) this total distance

        new_node = Node(p)
        if self.length < 2:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return None

        head = self.head
        base_distance = self.distance()
        min_distance = inf
        prev_when_min = self.head
        while head is not None:  # todo: first?/last case
            position_new_node = p

            # wrap linked list when end of tour
            if head.next is None:
                point_next_node = self.head.point
                dist_prev_to_next = head.point.distance_to(point_next_node)  # remove
            else:
                point_next_node = head.next.point
                dist_prev_to_next = head.point.distance_to(point_next_node)  # remove

            dist_prev_to_new = head.point.distance_to(position_new_node)  # add
            dist_new_to_next = new_node.point.distance_to(point_next_node)  # add

            new_dist = base_distance - dist_prev_to_next + dist_prev_to_new + dist_new_to_next
            if new_dist < min_distance:
                min_distance = new_dist
                prev_when_min = head
            head = head.next
        self._insert_at(p, prev_when_min)
