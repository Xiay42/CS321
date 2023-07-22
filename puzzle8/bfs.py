# type: ignore
import puzzle8 as p8
from typing import List
from collections import namedtuple, deque

Node = namedtuple('Node', ['state', 'steps'])

def breadth_first_search(state: int) -> List[int]:
	"""Finds path to solution via breadth-first search. Returns a list of
	squares that the blank moves to in order to get to solution.
	"""
	
	unvisited_nodes = deque()
	unvisited_nodes.append(Node(state, []))
	
	while unvisited_nodes:
		current_node = unvisited_nodes.popleft()
		
		if current_node.state == p8.solution():
			return current_node.steps
		
		for i in p8.neighbors(p8.blank_square(current_node.state)):
			unvisited_nodes.append(Node(
				state = p8.move_blank(current_node.state, i), 
				steps = current_node.steps + [i],
			))
