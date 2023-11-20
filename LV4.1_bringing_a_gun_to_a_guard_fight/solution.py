# Note: I lost my original solution using law of reflection somewhere
# this is the closest idea I could find to my solution:
# https://www.oasys.net/posts/google-foobar-programming-challenge/
# so I just optimized it a bit.

from itertools import product
import math 
def solution(dimensions, your_position, trainer_position, distance):
    # Record the angle and distance of the shots.
    methods = {}
    # Four quadrants on an x-y plane.
    quadrants = [(1,1), (-1,1), (-1,-1), (1,-1)]
    # Calculate the valid shots with the law of reflection.
    # Then mirror your_position and trainer_position into four quadrants.
    for quadrant in quadrants:
        for mirror in product(*[range(-(distance//-d)+1) for d in dimensions]):
            for position in your_position, trainer_position:
                x, y = [q * (m*d + (d-p if m%2 else p)) for q, m, d, p 
                        in zip(quadrant, mirror, dimensions, position)]
                # Calculate the distance the beam has traveled.
                trace = math.hypot(your_position[0]-x, your_position[1]-y)
                # This distance must not exceed the beam's max traveling capacity.
                if trace > distance:
                    continue
                # Calculate the angle of the shot.
                angle = math.atan2(your_position[0]-x, your_position[1]-y)
                # If the angle hasn't been found,
                # or it's been found, but we have a closer distance
                # (i.e., If we can hit the target with the same angle, 
                # the shorter distance should always be picked and 
                # no more reflection/traveling can happen after this distance.)
                if (angle not in methods or trace <= methods[angle][0]):
                    # Need to filter out the shots that are blocked by ourselves.
                    # Flag them using boolean so don't have to keep two dictionaries.
                    methods[angle] = (trace, True) if position != your_position\
                                     else (trace, False)
    return len([True for v in methods.values() if v[1]])