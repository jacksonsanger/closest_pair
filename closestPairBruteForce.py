from __future__ import annotations
from Point import Point
import math


class CPBruteForce:
    def distance(p1: Point, p2: Point):
        #compute the x and y components
        xDist = (p1.x - p2.x)**2
        yDist = (p1.y - p2.y)**2
        return math.sqrt(xDist + yDist)

    def CPBruteForce(P: list[Point]):
        #start min distance as the min of the first 2 points in input array.
        min = CPBruteForce.distance(P[0], P[1])
        p1 = None
        p2 = None
        for i in range(len(P)):
            for j in range(i+1, len(P)):
                dist = CPBruteForce.distance(P[i], P[j])
                if dist <= min:
                    min = dist
                    p1 = P[i]
                    p2 = P[j]
        return (p1, p2, min)
