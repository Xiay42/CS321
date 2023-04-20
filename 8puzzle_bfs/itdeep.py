# Michael and Lev
# 4.2.2023

import puzzle8 as p8
from typing import List

def iterative_deepening_search(state: int) -> List[int]:
	"""Finds path to solution via iterative deepening. Returns a list of
	squares that the blank moves to in order to get to solution.
	"""
	i=0
	while True:
		result = depth_first_search_with_depth_limit(state, i)
		if result != None:
			return result
		i+=1


def depth_first_search_with_depth_limit(state: int, depth_limit: int):
	"""Finds path to solution via depth-first search with depth limit. If no result is found, 
	returns a Result type with a false is_sucsess otherwise reutrns a result type with a 
	true is_sucsess and a list of squares that the blank moves to in order to get to solution.
	"""
	if state == p8._goal:
		return []
	if depth_limit != 0:
		for i in p8.neighbors(p8.blank_square(state)):
			result = depth_first_search_with_depth_limit(p8.move_blank(state, i), depth_limit-1)
			if result != None:
				return [i] + result
	return None

if __name__ == "__main__":
	state = p8.random_state(num_moves=1)
	p8.display(state) 
	print(depth_first_search_with_depth_limit(state, 2))