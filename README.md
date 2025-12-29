# OCTO Challenge 2025

## What is OCTO Challenge 2025?

OCTO Challenge 2025 is an annual competition that brings together developers, designers, and tech enthusiasts from around the world to solve real-world problems using innovative technology solutions. Participants are encouraged to collaborate, create, and showcase their skills in a competitive yet supportive environment.

## Sponsorship

Bentley Systems is proud to sponsor this event, providing resources and support to help participants succeed.

## How to Participate

1. You **must be a Bentley Systems colleague** to join the challenge.
2. Register on the official OCTO Challenge 2025 website.
3. Answer the challenge questions each week.

---

# Datasets

## Week 1: Statistical Analysis
**Problem:** Calculate the sum of all numbers strictly greater than two standard deviations away from the mean.

- Example Dataset: [ex1_1.txt](ex1_1.txt) (20 numbers)
- Full Dataset: [1.txt](1.txt) (1,000,001 numbers)

## Week 2: Binary Wordle
**Problem:** Find the correct 8-bit answer given guesses and their Hamming distances.

- Example Dataset: [ex2_2.txt](ex2_2.txt)
- Full Dataset: [2.txt](2.txt) (32 guess-distance pairs)

## Week 3: Reverse Polish Notation (RPN)
**Problem:** Evaluate mathematical expressions in Reverse Polish Notation and solve dependency graphs.

### Part 1: RPN Evaluation
- Example Dataset: [ex3_1.txt](ex3_1.txt)
- Full Dataset: [3_1.txt](3_1.txt) (RPN expressions)

### Part 2: Specification Requirements
- Requirements parsing and evaluation (embedded in solution code)

## Week 4: Graph Problems
**Problem:** Solve path-finding and task ordering challenges in graph structures.

### Part 1: Shortest Path with Time-dependent Edges
- Example Dataset: [ex4_1.txt](ex4_1.txt)
- Full Dataset: [4_1.txt](4_1.txt) (DOT format graph with timestep constraints)

### Part 2: Task Ordering with Topological Sort
- Example Dataset: [ex4_2.txt](ex4_2.txt)
- Full Dataset: [4_2.txt](4_2.txt) (Directed graph with dependencies)

---

# Solutions

## Week 1: Statistical Analysis
- [week1_part1.py](week1_part1.py) - Calculates sum of outliers (values > 2 standard deviations from mean)

**Approach:** Uses NumPy for efficient statistical calculations on large datasets.

## Week 2: Binary Wordle
- [week2_part1.py](week2_part1.py) - Finds the 8-bit answer using Hamming distance constraints
- [week2_part2.py](week2_part2.py) - Helper utilities for bit manipulation
- [conti_week2_part1.py](conti_week2_part1.py) - Alternative/continuation solution

**Approach:** Converts numbers to binary representation and uses intersection of possible candidates based on Hamming distance from each guess.

## Week 3: RPN and Specifications
- [week3_part1.py](week3_part1.py) - Evaluates Reverse Polish Notation expressions using a stack
- [week3_part2.py](week3_part2.py) - Parses specification requirements and builds dependency graph
- [week3_test.py](week3_test.py) - Test cases for validation

**Approach:** 
- Part 1: Stack-based RPN evaluation
- Part 2: Dependency resolution using requirement parsing and graph traversal

## Week 4: Graph Algorithms
- [week4_part1.py](week4_part1.py) - Counts shortest paths in time-dependent graphs
- [week4_part2.py](week4_part2.py) - Performs topological sort for task ordering

**Approach:**
- Part 1: BFS with state tracking for timestep parity (even/odd edges)
- Part 2: Kahn's algorithm for topological sorting with dependency resolution

---

# File Naming Convention

- `ex#_#.txt` - Example datasets for testing
- `#.txt` or `#_#.txt` - Full challenge datasets
- `week#_part#.py` - Solution implementations


