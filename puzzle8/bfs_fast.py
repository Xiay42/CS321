
# ASK:
# 1. Can I use single line if statments?
# 2. does he prefer concise code, or single use variable names that self document?
# 3. Is it normal to sometimes get hung up on large random seeds?
# 4. is it okay that I effectively have a while true in line 28?


# TODO: make sure var naming lines up with lectures
# TODO: remove main function


# type: ignore
import puzzle8 as p8
from typing import List
from collections import namedtuple, deque

Node = namedtuple('Node', ['state', 'steps'])

def breadth_first_search(state: int) -> List[int]:
	"""Finds path to solution via breadth-first search. Returns a list of
	squares that the blank moves to in order to get to solution.
	"""
	root_node = Node(state = state, steps=[])
	unvisited_nodes = deque()
	unvisited_nodes.append(root_node)
	
	while unvisited_nodes:
		current_node = unvisited_nodes.popleft()
		# if current_node.state == p8.solution(): return current_node.steps
		if p8.get_tile(current_node.state, 0) == 1 and p8.get_tile(current_node.state, 1) == 2 and p8.get_tile(current_node.state, 2) == 3:
			return breadth_first_search_middle_two(current_node)
		
		blank_square = p8.blank_square(current_node.state)
		for i in p8.neighbors(blank_square):
			new_leaf = p8.move_blank(current_node.state, i)
			new_steps = current_node.steps + [i]
			new_node = Node(state=new_leaf, steps=new_steps)
			unvisited_nodes.append(new_node)
			

def breadth_first_search_middle_two(root_node: Node) -> List[int]:
	"""Finds path to solution via breadth-first search. Returns a list of
	squares that the blank moves to in order to get to solution.
	"""
	# print("found top three")
	# p8.display(root_node.state)
	
	unvisited_nodes = deque()
	unvisited_nodes.append(root_node)
	
	while unvisited_nodes:
		current_node = unvisited_nodes.popleft()
		# if current_node.state == p8.solution(): return current_node.steps
		if p8.get_tile(current_node.state, 5) == 4 and p8.get_tile(current_node.state, 8) == 5:
			return breadth_first_search_last_four(current_node)
		
		blank_square = p8.blank_square(current_node.state)
		# valud neighbors are any neibors not in the following list
		neighbors = p8.neighbors(blank_square)
		exclude = [0, 1, 2]
		neighbors = [x for x in neighbors if x not in exclude]
		for i in neighbors:
			new_leaf = p8.move_blank(current_node.state, i)
			new_steps = current_node.steps + [i]
			new_node = Node(state=new_leaf, steps=new_steps)
			unvisited_nodes.append(new_node)


def breadth_first_search_last_four(root_node: Node) -> List[int]:
	"""Finds path to solution via breadth-first search. Returns a list of
	squares that the blank moves to in order to get to solution.
	"""
	# print("found first five")
	# p8.display(root_node.state)
	
	unvisited_nodes = deque()
	unvisited_nodes.append(root_node)
	
	while unvisited_nodes:
		current_node = unvisited_nodes.popleft()
		if current_node.state == p8.solution(): return current_node.steps
		
		blank_square = p8.blank_square(current_node.state)
		# valud neighbors are any neibors not in the following list
		neighbors = p8.neighbors(blank_square)
		exclude = [0, 1, 2, 5, 8]
		neighbors = [x for x in neighbors if x not in exclude]
		for i in neighbors:
			new_leaf = p8.move_blank(current_node.state, i)
			new_steps = current_node.steps + [i]
			new_node = Node(state=new_leaf, steps=new_steps)
			unvisited_nodes.append(new_node)

def main():
	"""Runs breadth-first search on a random puzzle and prints the solution.
	"""
	state = p8.random_state(num_moves=30)

	print("Starting puzzle:")
	p8.display(state)
	
	print("The steps to solve this puzzle are:")
	path = breadth_first_search(state)
	print(path)

if __name__ == "__main__":
	main()