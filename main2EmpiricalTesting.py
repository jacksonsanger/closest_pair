from __future__ import annotations
from time import time
from Point import Point
from closestPairBruteForce import CPBruteForce
from closestPairDAC import closestPairDAC
from random import random

def main():
    # #Run time is O(n^2)
    # print("Empirical Testing of BruteForce:")
    # #print out labels for each column in a readable way
    # print(f"n:\telapsed time:\t\ttime per call:")
    # #initialize a variable for the number of times we will repeat the algorithm
    # num_trials = 50000
    # #loop over varying input sizes
    # for n in [10, 20, 40, 80]:
    #     #generate array of random test points in a 100x100 grid
    #     test_points = []
    #     for i in range(n):
    #         x = random() * 100
    #         y = random() * 100
    #         test_points.append(Point(x, y))
    #     #start the timer
    #     start = time()
    #     #repeat the algorithm num trials times
    #     for i in range(num_trials):
    #         #run the algorithm
    #         CPBruteForce.CPBruteForce(test_points)
    #     #stop the timer
    #     stop = time()
    #     #calculate elapsed time
    #     elapsed_time = stop - start
    #     #print out the results in a way that is easy to read
    #     print(f"{n}\t{elapsed_time}\t{elapsed_time/num_trials}")

    #Run time is O(nlogn)
    print("Empirical Testing of Divide and Conquer:")
    #print out labels for each column in a readable way
    print(f"n:\telapsed time:\t\ttime per call:")
    #initialize a variable for the number of times we will repeat the algorithm
    num_trials = 3000
    #loop over varying input sizes
    for n in [100, 200, 400, 800, 1600, 3200]:
        #generate array of random test points in a 100x100 grid
        test_points = []
        for i in range(n):
            x = random() * 100
            y = random() * 100
            test_points.append(Point(x, y))
        #start the timer
        start = time()
        #repeat the algorithm num trials times
        for i in range(num_trials):
            #run the algorithm
            closestPairDAC.closestPairDACStarter(test_points)
        #stop the timer
        stop = time()
        #calculate elapsed time
        elapsed_time = stop - start
        #print out the results in a way that is easy to read
        print(f"{n}\t{elapsed_time}\t{elapsed_time/num_trials}")

if __name__ == "__main__":
    main()