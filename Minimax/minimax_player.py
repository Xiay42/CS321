
"""Minimax game player. You should modify the choose_move code for the
MinimaxPlayer class. You should also modify the heuristic function, which
should return a number indicating the value of that board position.
"""

from __future__ import annotations
from common_values import (EMPTY, MAX_PLAYER, RED, YELLOW)
from common_values import EMPTY, MAX_PLAYER
from game_board import GameBoard, Location
from typing import Optional, Callable
from collections import namedtuple
from typing import Optional, List
from player import Player
import random


Helper_Return = namedtuple('Helper_Return', ['moves', 'value'])
isSmaller, isLarger = lambda a,b: a < b, lambda a,b: a > b


def is_legal_move_alternate(board, location) -> bool:
	''' Returns whether or not move is legal.'''
	piece = -board.get_active_player()
	if board.grid[location.row][location.column] != EMPTY or piece != YELLOW and piece != RED\
		or board.in_second_stage() and board.num_adjacent_friendlies(location, piece) < 2:
		return False
	return True

def get_legal_moves_alternate(board) -> List[Location]:
	"""Returns a list of Locations that represent legal moves that can be
	made.
	"""
	legal_moves = []
	for row in range(1, board.size+1):
		for column in range(1, board.size+1):
			location = Location(row, column)
			if is_legal_move_alternate(board, location):
				legal_moves.append(location)
	return legal_moves

def heuristic(board: GameBoard) -> float:
	"""Measure the value of the game board, where a high number means that is
	good for the max player, and a low number means that it is good for the min
	player. The maximum possible value should be 1, which is the value that
	should be returned if the board supplied is a guaranteed win for the max
	player. Likewise, the minimum possible value should be a -1, which is a
	guaranteed win for the min player.
	"""
	
	num_of_blank_squares = sum([1
		for row in range(1, board.size + 1)
		for col in range(1, board.size + 1)
		if board.grid[row][col] != EMPTY])-2 if board.in_second_stage() else 1
	
	number_of_availble_moves_for_opp = len(get_legal_moves_alternate(board)) if board.in_second_stage() else random.random()
	number_of_availble_moves_for_self = len(board.get_legal_moves()) if board.in_second_stage() else random.random()
	
	if board.get_active_player() == MAX_PLAYER: 
		number_of_availble_moves_for_max = number_of_availble_moves_for_self
		number_of_availble_moves_for_min = number_of_availble_moves_for_opp
	else:
		number_of_availble_moves_for_max = number_of_availble_moves_for_opp
		number_of_availble_moves_for_min = number_of_availble_moves_for_self

	
	max_moves_div_open_squares = number_of_availble_moves_for_max/num_of_blank_squares
	min_moves_div_open_squares = number_of_availble_moves_for_min/num_of_blank_squares

	return max_moves_div_open_squares - min_moves_div_open_squares

class MinimaxPlayer(Player):
	"""Minimax player: uses minimax to find the best move."""
	def __init__(self,
				 heuristic: Callable[[GameBoard], float],
				 plies: int) -> None:
		self.heuristic = heuristic
		self.plies = plies
	
	def choose_move(self, board: GameBoard) -> Optional[Location]:
		if board.get_active_player() == MAX_PLAYER:
			return self.choose_move_helper(-2, isLarger, board, self.plies-1).moves # type: ignore (do max behavior)
		else:
			return self.choose_move_helper(2, isSmaller, board, self.plies-1).moves # type: ignore (do min behavior)
	
	def choose_move_helper(self, value, comparison_function, board, plies):
		moves = None
		for i in board.get_legal_moves():
			new_board = board.make_move(i)
			if new_board != None:
				if plies == 0:
					recursive_result = heuristic(new_board)
				else:
					recursive_result = self.minimax_search_utility(new_board, plies - 1)
				if comparison_function(recursive_result, value):
					value = recursive_result
					moves = i
		return Helper_Return(moves,value)
	
	def minimax_search_utility(self, board: GameBoard, plies):
		if board.get_active_player() == MAX_PLAYER:
			return_value = self.choose_move_helper(-1, isLarger, board, plies).value
			return return_value #do max behavior
		else:
			return_value = self.choose_move_helper(1, isSmaller, board, plies).value
			return return_value #do min behavior
