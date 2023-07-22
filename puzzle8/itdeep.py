# type: ignore
from typing import List, Optional
from itertools import count
from inspect import getfullargspec

import puzzle8 as p8
import time

def iterative_deepening_search(state: int) -> List[int]:
	"""Finds path to solution via iterative deepening. Returns a list of
	squares that the blank moves to in order to get to solution.
	"""
	for i in count():
		result = depth_first_search_with_depth_limit(state, i)
		if result != None:
			return result

def depth_first_search_with_depth_limit(state: int, depth_limit: int) -> Optional[List[int]]:
	"""Finds path to solution via depth-first search with depth limit. If no result is found, 
	returns a Result type with a false is_sucsess otherwise reutrns a result type with a 
	true is_sucsess and a list of squares that the blank moves to in order to get to solution.
	"""
	if state == p8.solution():
		return []
	if depth_limit != 0:
		for i in p8.neighbors(p8.blank_square(state)):
			result = depth_first_search_with_depth_limit(p8.move_blank(state, i), depth_limit-1)
			if result != None:
				return [i] + result
	return None

STATES = [
	[
		1, 2, 3,
		8, 0, 4,
		7, 6, 5
	],[
		1, 2, 3,
		8, 4, 0,
		7, 6, 5
	],[
		1, 2, 0,
		8, 4, 3,
		7, 6, 5
	],[
		1, 0, 2,
		8, 4, 3,
		7, 6, 5
	],[
		0, 1, 2,
		8, 4, 3,
		7, 6, 5
	],[
		8, 1, 2,
		0, 4, 3,
		7, 6, 5
	],[
		8, 1, 2,
		4, 0, 3,
		7, 6, 5
	],[
		8, 1, 2,
		4, 3, 0,
		7, 6, 5
	],[
		8, 1, 2,
		4, 3, 5,
		7, 6, 0
	],[
		8, 1, 2,
		4, 3, 5,
		7, 0, 6
	],[
		8, 1, 2,
		4, 0, 5,
		7, 3, 6
	],[
		8, 0, 2,
		4, 1, 5,
		7, 3, 6
	],[
		0, 8, 2,
		4, 1, 5,
		7, 3, 6
	],[
		4, 8, 2,
		0, 1, 5,
		7, 3, 6
	]
]

def main():
	"""Generate the results seen in README.txt
	"""
	for depth_of_solution, state in enumerate(STATES):
		time_result = []
		for algo in [iterative_deepening_search, depth_first_search_with_depth_limit]:
			start = time.time()
			algo(*[p8.state(state)] + ([depth_of_solution] if len(getfullargspec(algo).args)==2 else []))
			time_result += [time.time() - start]
		
		print(
			"When the solution is of depth",
			depth_of_solution,
			"the time to find the result using iteritive deepening is",
			round(time_result[0]/time_result[1], 2),
			"times longer than Depth First Search"
		)

if __name__ == "__main__":
	main()