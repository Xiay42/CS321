# type: ignore
import puzzle8 as p8
from typing import List
from collections import namedtuple
from itertools import count

Result = namedtuple('Result', ['is_success', 'int_list'])

def iterative_deepening_search(state: int) -> List[int]:
	"""Finds path to solution via iterative deepening. Returns a list of
	squares that the blank moves to in order to get to solution.
	"""
	for i in count():
		result = depth_first_search_with_depth_limit(state, i)
		if result.is_success: return result.int_list

def depth_first_search_with_depth_limit(state: int, depth_limit: int) -> Result:
	"""Finds path to solution via depth-first search with depth limit. If no result is found, 
	returns a Result type with a false is_sucsess otherwise reutrns a result type with a 
	true is_sucsess and a list of squares that the blank moves to in order to get to solution.
	"""
	if state == p8.solution(): return Result(is_success=True, [])
	if depth_limit > 0:
		for i in p8.neighbors(p8.blank_square(state)):
			result = depth_first_search_with_depth_limit(p8.move_blank(state, i), depth_limit - 1)
			if result.is_success: return Result(True, [i] + result.int_list)
	return Result(is_success=False, int_list=[])

def main():
	"""Runs breadth-first search on a random puzzle and prints the solution.
	"""
	state = p8.random_state(num_moves=10)

	print("Starting puzzle:")
	p8.display(state)

	print("The steps to solve this puzzle are:")
	path = iterative_deepening_search(state)
	print(path)

if __name__ == "__main__":
	main()