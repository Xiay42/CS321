# type: ignore
from heapq import heappush, heappop
from collections import namedtuple
from inspect import getfullargspec
from typing import List
from time import time

import puzzle8 as p8
import itdeep

Node = namedtuple('Node', ['state', 'steps'])

def num_wrong_tiles(state) -> int:
	"""Given a puzzle, returns the number of tiles that are in the wrong
	location. Does not count the blank space.
	"""
	return sum(1 for i in range(9) if
		p8.get_tile(state, i) != 0 and
		p8.get_tile(state, i) != p8.get_tile(p8.solution(), i)
	)

def manhattan_distance_helper(i, state):
	active_tile = p8.get_tile(state, i)
	if active_tile == 0:
		return 0
	
	current = p8.xy_location(i)
	goal = p8.xy_location([1, 2, 3, 8, 0, 4, 7, 6, 5].index(active_tile))
	return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

def manhattan_distance(state):
	"""Given a puzzle, returns the Manhattan distance to the solution state.
	Does not count the distance from blank space to its correct location as
	part of the distance.
	"""
	return sum(manhattan_distance_helper(i, state) for i in range(9))

def astar_search(state: int, heuristic) -> List[int]:
	"""Finds path to solution via A* search, using the provided heuristic.
	Returns a list of squares that the blank moves to in order to get to
	solution.
	"""
	unvisited_nodes = []
	heappush(unvisited_nodes, (heuristic(state), Node(state, [])))
	
	while unvisited_nodes:
		_, current_node = heappop(unvisited_nodes)
		
		if current_node.state == p8.solution():
			return current_node.steps
		
		for i in p8.neighbors(p8.blank_square(current_node.state)):
			new_node = Node(p8.move_blank(current_node.state, i), current_node.steps + [i])
			heappush(unvisited_nodes, (heuristic(new_node.state) + len(new_node.steps), new_node))

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
		for algo in [itdeep.iterative_deepening_search, astar_search]:
			start = time()
			algo(*[p8.state(state)] + ([num_wrong_tiles] if len(getfullargspec(algo).args)==2 else []))
			time_result += [time() - start]
		
		print(
			"When the solution is of depth",
			depth_of_solution,
			"the time to find the result using iteritive deepening is",
			round(time_result[0]/time_result[1], 2),
			"times longer than A*",
			# "\t iterative_deepening_search took ",
			# time_result[0],
			# "\t astar_search took ",
			# time_result[1]
		)

if __name__ == "__main__":
	main()