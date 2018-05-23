#
# point_explorer.py
#
# The beginnings of a client program for Point objects
#
# CS 111
#

from point import *

p1 = Point(7, 24)
p2 = Point(0, -7)

print('p1 has coordinates', p1)   # calls __repr__
print('p2 has coordinates', p2)   # calls __repr__

dist1 = p1.distance_from_origin()
dist2 = p2.distance_from_origin()
print(p1, 'is', dist1, 'away from the origin')
print(p2, 'is', dist2, 'away from the origin')

print('moving p1 down 7 units...')
p1 = p1.move_down(7)
print('p1 now has coordinates', p1)

p3 = Point(int(input("x: ")), int(input("y: ")))
dist3 = p3.distance_from_origin()
print(p3, 'is', dist3, 'away from the origin')
p3.flip()
print("New coordinate of p3 is", p3)
quadrant_p3 = p3.quadrant()
if quadrant_p3 == 0:
    print("p3 is not on the axis.")
else:
    print("p3 is on quadrant", quadrant_p3)
