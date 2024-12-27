from __future__ import annotations
from Point import Point
from closestPairBruteForce import CPBruteForce
import math

class closestPairDAC:
    def distance(p1: Point, p2: Point):
        #compute the x and y components
        xDist = (p1.x - p2.x)**2
        yDist = (p1.y - p2.y)**2
        return math.sqrt(xDist + yDist)
    
    def closestPairDACStarter(P: list[Point]):
        #sort P by X coordinates and y coordinates
        x = sorted(P, key = lambda point: point.x)
        y = sorted(P, key = lambda point: point.y)
        return closestPairDAC.closestPairDAC(P, x, y)
    
    def closestPairDAC(P: list[Point], X: list[Point], Y: list[Point]):
        #base case, we have 3 points. simply run brute force
        #P is the entire collection of points
        #X is all points in P sorted with respect to X coord
        #Y is all points in P sorted with respect to Y coord
        if len(P) <= 3:
            return CPBruteForce.CPBruteForce(P)
        #compute the midpoint index of the array
        mid = len(X)//2
        #compute pl and pR by splitting X at the midpoint
        pL = X[:mid]
        pR = X[mid:]
        #compute xL and Xr, which is the same as p1 and p2
        xL = X[:mid]
        xR = X[mid:]
        #compute yL and yR, by taking advantage of the fact that the elements are presorted
        yL = []
        yR = []
        for i in range(len(Y)):
            #compare each points x component to the mid point to determine if it should go in left or right
            if Y[i].x <= X[mid-1].x:
                yL.append(Y[i])
            else:
                yR.append(Y[i])
        #recursively find the minimums on the left and right sides
        leftDelta = closestPairDAC.closestPairDAC(pL, xL, yL)
        rightDelta = closestPairDAC.closestPairDAC(pR, xR, yR)

        #after finding the two mins, compute smallest overall (delta)
        #2 is the index of the actual distance value in the tuple
        delta = min(leftDelta[2], rightDelta[2])

        #finally, compute Y', the points that are within a 2*delta band from the midpoint.
        #is going to be sorted with respect to y coord because Y is sorted
        yprime = []
        #get the actual x coordinate of the midpoint to compute the bounds of the strip
        leftBound = X[mid-1].x - delta
        rightbound = X[mid-1].x + delta
        for i in range(len(Y)):
            if Y[i].x >= leftBound and Y[i].x <= rightbound:
                yprime.append(Y[i])
        
        #now that we have y prime, we can iterate through each point and compare to the 7 other points
        #keep track of the smallest distance found within the strip
        stripDelta = delta + 1
        p1 = None
        p2 = None
        for i in range(len(yprime)):
            #to avoid index error, check if the end of the array is smaller than adding 7 to the index
            for j in range(i+1, min(i+7, len(yprime))):
                d = closestPairDAC.distance(yprime[i], yprime[j])
                if d < stripDelta:
                    stripDelta = d
                    p1 = yprime[i]
                    p2 = yprime[j]
        #finally, if the smallest value was in the strip, return that distance and the corresponding points
        if stripDelta < delta:
            return p1, p2, stripDelta
        #otherwise, return the correct solution tuple based on which delta was smaller, left or right
        elif leftDelta[2] < rightDelta[2]:
            return leftDelta
        else:
            return rightDelta

