from __future__ import annotations
from Point import Point
from closestPairBruteForce import CPBruteForce
from closestPairDAC import closestPairDAC
from random import random

def main():
    #generate test array of size 10,000 in a 100 x 100 grid
    n = 10000
    test = []
    for i in range(n):
        randx = random() * 100
        randy = random() * 100
        test.append(Point(randx, randy))
    
    print(CPBruteForce.CPBruteForce(test))
    print(closestPairDAC.closestPairDACStarter(test))


if __name__ == "__main__":
    main()