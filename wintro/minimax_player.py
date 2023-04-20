"""Minimax game player. You should modify the choose_move code for the
MinimaxPlayer class. You should also modify the heuristic function, which
should return a number indicating the value of that board position.

Feel free to add additional helper methods or functions.
"""

from __future__ import annotations
from common_values import EMPTY, MAX_PLAYER, MIN_PLAYER
from game_board import GameBoard, Location
from typing import Optional, Callable
from player import Player


def heuristic(board: GameBoard) -> float:
	"""Measure the value of the game board, where a high number means that is
	good for the max player, and a low number means that it is good for the min
	player. The maximum possible value should be 1, which is the value that
	should be returned if the board supplied is a guaranteed win for the max
	player. Likewise, the minimum possible value should be a -1, which is a
	guaranteed win for the min player.

	(The textbook indicates at some point in passing that this heuristic should
	range from 0 to 1, but there's no theoretical reason for 0 as opposed to -1
	for the bottom end, and the asymmetry just makes everything more
	complicated. What does matter is that the heuristic value for a
	non-terminal state should never be bigger in magnitude than that for an
	terminal state, because that would suggest that it the non-terminal state
	is more conclusive than a terminal state (which it can't be).
	"""
	
	number_of_availble_moves = len(board.get_legal_moves())
	num_of_blank_squares = 0
	for row in range(1, board.size+1):
			for col in range(1, board.size+1):
				if board.grid[row][col] != EMPTY:
					num_of_blank_squares += 1
				
	# size_of_board = len(board.grid) * len(board.grid[0])
	return (number_of_availble_moves / num_of_blank_squares) * board.get_active_player()


class MinimaxPlayer(Player):
	"""Minimax player: uses minimax to find the best move."""
	def __init__(self,
				 heuristic: Callable[[GameBoard], float],
				 plies: int) -> None:
		self.heuristic = heuristic
		self.plies = plies
		
	def minimax_search_utility(self, board: GameBoard, plies, alpha, beta) -> float:
		if plies == 0:
			return heuristic(board)
		elif board.get_active_player() == MAX_PLAYER:
			#do max behavior
			value:float = -2
			for i in board.get_legal_moves():
				new_board = board.make_move(i)
				#if new_board != None:
				value = max(value, self.minimax_search_utility(new_board, plies-1, alpha, beta))
				if value >= beta:
					return value
				alpha = max(alpha, value)
			return value
		elif board.get_active_player() == MIN_PLAYER:
			# do min behavior
			value:float = 2
			for i in board.get_legal_moves():
				new_board = board.make_move(i)
				#if new_board != None:
				value = min(value, self.minimax_search_utility(new_board, plies - 1, alpha, beta))
				if value <= alpha:
					return value
				beta = min(beta, value)
			return value


	def choose_move(self, board: GameBoard) -> Optional[Location]:
		value = -2
		move = None
		# if in early game, pick random 
		if not board.in_second_stage():
			return board.get_random_legal_move()
		if board.get_active_player() == MAX_PLAYER:
			#do max behavior
			for i in board.get_legal_moves():
				new_board = board.make_move(i)
				if new_board != None:
					value = max(value, self.minimax_search_utility(new_board, self.plies, -2, 2))
					move = i
			return move
		elif board.get_active_player() == MIN_PLAYER:
			#do min behavior
			value= 2
			for i in board.get_legal_moves():
				new_board = board.make_move(i)
				if new_board != None:
					value = min(value, self.minimax_search_utility(new_board, self.plies, -2, 2))
					move = i
		return move