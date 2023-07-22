"""MCTS game player starter code. Fill in the methods as indicated below.

Originally based on work by:
@author Bryce Wiedenbeck
@author Anna Rafferty
@author Dave Musicant
"""

from __future__ import annotations
from common_values import MIN_PLAYER, MAX_PLAYER
from game_board import GameBoard, Location
from typing import Optional
from player import Player
import math

class MctsPlayer(Player):
	"""Uses MCTS to find the best move.

	Plays random games from the root node to a terminal state. In each playout,
	play proceeds according to UCB while all children have been expanded. The
	first node with unexpanded children has a random child expanded. After
	expansion, play proceeds by selecting uniform random moves. Upon reaching a
	terminal state, values are propagated back along the expanded portion of
	the path. After all playouts are completed, the move generating the highest
	value child of root is returned.
	"""

	def __init__(self, playouts, ucb_const):
		self.playouts = playouts
		self.ucb_const = ucb_const

	def choose_move(self, board) -> Optional[Location]:
		root = MctsNode(board, None, self.ucb_const)
		return root.choose_move_via_mcts(self.playouts)


class MctsNode:
	"""Node used in MCTS. It is a wrapper to contain a board/state as a node
	within a tree."""

	def __init__(self, state: GameBoard, parent: Optional[MctsNode],
				 ucb_const: float) -> None:
		"""Constructor for a new node representing game state
		state. parent_node is the Node that is the parent of this
		one in the MCTS tree.
		"""

		self.state = state
		self.parent = parent
		self.ucb_const = ucb_const

		# All of the known children for this node. To get to each child, a move
		# (specificed by a Location) is used.
		self.children: dict[Location, MctsNode] = {}

		# Stats of games played out from this node, from the perspective of the
		# player at this node.
		self.wins_for_this_player = 0
		self.total_games_for_this_player = 0

		# All legal moves that can me made from this node; useful to have once
		# to avoid recalculating later. Your code will be faster if you use
		# this value rather than calculating it when you need it.
		self.legal_moves = self.state.get_legal_moves()

		# You may add additional fields if needed below.
		self.wins_for_other_player = lambda: self.total_games_for_this_player-self.wins_for_this_player


	def get_win_percentage_if_chosen_by_parent(self) -> float:
		"""Gets the win percentage for the current node, from the perspective
		of the parent node that is trying to decide whether or not to select
		this node.

		You will need this for computing the UCB weight when doing playouts,
		and also for making the final choice on which move to make.
		"""
		return self.wins_for_other_player() / self.total_games_for_this_player

	def get_UCB_weight_from_parent_perspective(self):
		"""Weight from the UCB formula for this node, when used by its parent
		to select a node proportionally to its weight. The win percentage
		aspect of this formula must be from the parent's perspective, since
		that is the node making the decision.

		You will need to use this as part of the selection phase when doing
		playouts.
		"""
		if self.parent:
			return self.get_win_percentage_if_chosen_by_parent() + self.ucb_const * math.sqrt(
				math.log(self.parent.total_games_for_this_player)/self.total_games_for_this_player)

	def update_play_counts(self, outcome: int) -> None:
		"""Updates the total games played from this node, as well as the number
		of wins from this node for the current player.

		You will need this for backpropagating wins/losses back up the tree.

		outcome: +1 for 1st player win, -1 for 2nd player win.
		"""
		if self.parent: self.parent.update_play_counts(outcome)
		self.total_games_for_this_player += 1
		
		if (self.state.get_active_player() == MAX_PLAYER and outcome == 1) or\
			(self.state.get_active_player() == MIN_PLAYER and outcome == -1):
			self.wins_for_this_player += 1
		
	def random_playout(self, gameboard: GameBoard) -> GameBoard:
		new_move = gameboard.get_random_legal_move()
		if not new_move: return gameboard 
		
		new_gameboard = gameboard.make_move(new_move)
		if not new_gameboard: return gameboard
		
		return self.random_playout(new_gameboard)


	def choose_move_via_mcts(self, playouts: int) -> Optional[Location]:
		"""Select a move by Monte Carlo tree search. Plays playouts random
		games from the root node to a terminal state. In each playout, play
		proceeds according to UCB while all children have been expanded. The
		first node with unexpanded children has a random child expanded. After
		expansion, play proceeds by selecting uniform random moves. Upon
		reaching a terminal state, values are propagated back along the
		expanded portion of the path. After all playouts are completed, the
		move generating the highest value child of root is returned.

		Returns None if no legal moves are available. If playouts is 0, returns
		a random choice from the legal moves.

		You will undoubtedly want to use helper functions when writing this,
		both some that I've provided, as well as helper functions of your own.
		"""
		
		for _ in range(playouts + 1):
			node = self
			# selection
			while node.legal_moves and len(node.legal_moves) == len(node.children):
				node = node.children[max(
					map(lambda child: (node.children[child].get_UCB_weight_from_parent_perspective(), child),
					node.children), key=lambda x: x[0])[1]]
			# expansion
			if node.state.get_legal_moves():
				unexplored_child = None
				for child in node.state.get_legal_moves():
					if child not in node.children: unexplored_child = child
				child_state = node.state.make_move(unexplored_child)
				if unexplored_child and child_state:
					node.children[unexplored_child] = MctsNode(child_state, node, node.ucb_const)
					# simulation
					outcome = node.random_playout(child_state)
					# backpropagation
					outcome_value = -1 if outcome.get_active_player() == MAX_PLAYER else 1
					node.children[unexplored_child].update_play_counts(outcome_value)
		children = []
		for child in self.children: children.append((self.children[child].get_UCB_weight_from_parent_perspective(), child))
		return max(children, key=lambda x: x[0])[1] if children else None
