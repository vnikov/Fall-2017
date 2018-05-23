#
# point.py
#
# The beginnings of a class for Point objects
#
# CS 111
#

## Fill in your answers to the questions in Task 0 below.
##
## 1. The constructor is called: __init__
##
##    Every Point object has attributes called: x and y
##
##    To create the specified Point objects from the Shell:
##
##        >>> p1 = Point(3, 4)
##        >>> p2 = Point(-5, -12)
##
## 3. The correct call is:  
##
##        >>> c. p1.distance_from_origin()
##
## 4. The move_down() method does the following:
##
##    It doesn't need to return a value because: the function needs to only
##                                               modify the y value.
##
##
## 5. We see the following:
##
##        >>> p1 == p2
##        False
##
##        >>> p1 == p3
##       True
 
import math

class Point:
    """ A class for objects that represent points in
        the Cartesian plane.
    """
    
    def __init__(self, init_x, init_y):
        """ constructor for a Point object that represents a point
            with coordinates (init_x, init_p1 = Point(3, 4)y)
        """
        self.x = init_x
        self.y = init_y

    def distance_from_origin(self):
        """ computes and returns the distance of the called Point object
            (self) from the origin (i.e., from (0, 0))
        """
        dist = math.sqrt(self.x**2 + self.y**2)
        return dist

    def move_down(self, amount):
        """ moves the called Point object (self) in a downwards
            direction by the specified amount
        """
        self.y -= amount

    def __repr__(self):
        """ returns a string representation for the called Point
            object (self)
        """
        s = '(' + str(self.x) + ', ' + str(self.y) + ')'
        return s

    def quadrant(self):
        """ returns the number of the quadrant (if any) in which the called
    Point object (self) falls """
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0

    def __eq__(self, other):
        """ compare the internals of the objects """
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def flip(self):
        """ negates and swaps the coordinates of the called Point object """
        negated_x = -1 * self.x
        self.x = -1 * self.y
        self.y = negated_x

    def in_same_quadrant(self, other):
        """ returns True if the called Point object and the other Point object
        are in the same quadrant, and False otherwise """
        if self.x == 0 or self.y == 0 or other.x == 0 or other.y == 0:
            return False
        elif self.quadrant() == other.quadrant():
            return True
        else:
            return False
