# For Testing
to run the test in a clean terminal:
```
clear; python3 -m pytest -vrP astar_test.py 
```


to view which functions take the most time:
```
python -m cProfile -o output.prof astar.py
snakeviz output.prof
```

# Discussing Results Prompt
Compare the running time across both heuristics, and compare with iterative deepening from the previous assignment. 
Indicate what you’ve learned about the relative timing in a readme.txt file that summarizes the results.

# Procuedure 
Consider the following test: For 5 < n < 14, generate a puzzle who's optimal solution is depth n
Below are the relation between the run times of A* and iterative deapening search, the first table is with
manhattan distance, the second is with number of wrong tiles.

# Result
When the solution is of depth 3 the time to find the result using iteritive deepening is 2.1 times longer than A*
When the solution is of depth 4 the time to find the result using iteritive deepening is 2.35 times longer than A*
When the solution is of depth 5 the time to find the result using iteritive deepening is 6.38 times longer than A*
When the solution is of depth 6 the time to find the result using iteritive deepening is 30.84 times longer than A*
When the solution is of depth 7 the time to find the result using iteritive deepening is 74.5 times longer than A*
When the solution is of depth 8 the time to find the result using iteritive deepening is 146.79 times longer than A*
When the solution is of depth 9 the time to find the result using iteritive deepening is 390.05 times longer than A*
When the solution is of depth 10 the time to find the result using iteritive deepening is 1286.48 times longer than A*
When the solution is of depth 11 the time to find the result using iteritive deepening is 2994.68 times longer than A*
When the solution is of depth 12 the time to find the result using iteritive deepening is 5711.67 times longer than A*
When the solution is of depth 13 the time to find the result using iteritive deepening is 13205.05 times longer than A*


When the solution is of depth 0 the time to find the result using iteritive deepening is 1.42 times longer than A*
When the solution is of depth 1 the time to find the result using iteritive deepening is 0.79 times longer than A*
When the solution is of depth 2 the time to find the result using iteritive deepening is 1.43 times longer than A*
When the solution is of depth 3 the time to find the result using iteritive deepening is 2.86 times longer than A*
When the solution is of depth 4 the time to find the result using iteritive deepening is 3.04 times longer than A*
When the solution is of depth 5 the time to find the result using iteritive deepening is 10.62 times longer than A*
When the solution is of depth 6 the time to find the result using iteritive deepening is 18.59 times longer than A*
When the solution is of depth 7 the time to find the result using iteritive deepening is 50.99 times longer than A*
When the solution is of depth 8 the time to find the result using iteritive deepening is 66.34 times longer than A*
When the solution is of depth 9 the time to find the result using iteritive deepening is 334.48 times longer than A*
When the solution is of depth 10 the time to find the result using iteritive deepening is 745.36 times longer than A*
When the solution is of depth 11 the time to find the result using iteritive deepening is 833.49 times longer than A*
When the solution is of depth 12 the time to find the result using iteritive deepening is 589.14 times longer than A*
When the solution is of depth 13 the time to find the result using iteritive deepening is 362.14 times longer than A*

Notice that as the depth increases the difference between algorthims increase 

# Analysis
It is clear that A* is magnitudes faster than iterative deepening. And as the problem gets more complex 
A*'s benifits increase.

manhattan_distance is a significantly better heuristic than num_wrong_tiles

