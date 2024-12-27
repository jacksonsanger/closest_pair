# Closest Pair Problem

This project implements two algorithms to solve the Closest Pair Problem, which identifies the two points in a 2D space with the minimum Euclidean distance.

## Features
- **Brute Force Algorithm**: Computes distances between all pairs of points and finds the minimum.
- **Divide and Conquer Algorithm**: Uses recursive techniques to divide the point set, compute distances for subsets, and merge results efficiently.

## File Structure
- `closestPairBruteForce.py`: Implementation of the brute force method.
- `closestPairDAC.py`: Implementation of the divide-and-conquer method.
- `Point.py`: Simple class representing 2D points with (x, y) coordinates.
- `main1SameTestArrays.py`: Tests both algorithms on identical sets of randomly generated points to validate correctness.
- `main2EmpiricalTesting.py`: Benchmarks the runtime of both algorithms on random datasets of varying sizes.

## How It Works
1. **Brute Force Approach**:
   - Iterates through all pairs of points in the dataset.
   - Calculates the Euclidean distance for each pair.
   - Tracks the minimum distance and the corresponding pair.

2. **Divide and Conquer Approach**:
   - Sorts the points by x-coordinate.
   - Recursively divides the set into smaller subsets.
   - Computes the closest pair in each subset and merges results.
   - Handles boundary cases efficiently using a strip-based approach for cross-subset pairs.

## Example Usage
Run the provided scripts to test and benchmark the algorithms:
- Use `main1SameTestArrays.py` to compare results from both algorithms on identical data inputs.
- Use `main2EmpiricalTesting.py` to analyze runtime for datasets with increasing sizes.

## Highlights
- Implements efficient geometric techniques in the divide-and-conquer solution for improved performance on large datasets.
- Provides detailed runtime comparisons to demonstrate algorithmic efficiency.
