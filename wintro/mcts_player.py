"""MCTS game player starter code. Fill in the methods as indicated below.

Feel free to add additional helper methods or functions.

Originally based on work by:
@author Bryce Wiedenbeck
@author Anna Rafferty
@author Dave Musicant
"""

from __future__ import annotations
import random
from game_board import GameBoard, Location
from typing import Optional
from player import Player
import math
from collections import namedtuple


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
        # self.value = namedtuple(state, ["p1_win", "p2_win", "total_sim"])
        self.ucb_const = ucb_const

        # All of the known children for this node. To get to each child, a move
        # (specificed by a Location) is used.
        # self.children: dict[Location, MctsNode] = {} 
        self.children: dict[state, MctsNode] = {}

        # Stats of games played out from this node, from the perspective of the
        # player at this node.
        self.wins_for_this_player = 0
        self.wins_for_other_player = 0
        self.total_games_for_this_player = 0

        # All legal moves that can me made from this node; useful to have once
        # to avoid recalculating later. Your code will be faster if you use
        # this value rather than calculating it when you need it.
        self.legal_moves = self.state.get_legal_moves()

        # You may add additional fields if needed below.

    def get_children_state (self):
        for i in self.state.get_legal_moves:
            new_board = self.state.make_move(i)
            self.children[new_board, self]

    def get_win_percentage_if_chosen_by_parent(self) -> float:
        """Gets the win percentage for the current node, from the perspective
        of the parent node that is trying to decide whether or not to select
        this node.

        You will need this for computing the UCB weight when doing playouts,
        and also for making the final choice on which move to make.
        """
        win_percentage_parent = self.wins_for_other_player/self.total_games_for_this_player
        return win_percentage_parent
    
    def get_UCB_weight_from_parent_perspective(self) -> float:
        """Weight from the UCB formula for this node, when used by its parent
        to select a node proportionally to its weight. The win percentage
        aspect of this formula must be from the parent's perspective, since
        that is the node making the decision.

        You will need to use this as part of the selection phase when doing
        playouts.
        """
        optimization_term = self.get_win_percentage_if_chosen_by_parent
        exploration_term = self.ucb_const * math.sqrt((self.parent.num of time been visited)/(self.total_games_for_this_player))
        UCB = optimization_term + exploration_term 
        return UCB
        #haven't write where to store p1_win, p2_win and total matches.

    def update_play_counts(self, outcome: int) -> None:
        """Updates the total games played from this node, as well as the number
        of wins from this node for the current player.

        You will need this for backpropagating wins/losses back up the tree.

        outcome: +1 for 1st player win, -1 for 2nd player win.
        """
        if outcome == 1:
            self.match_tuple[0] = self.match_tuple[0] + 1

        if outcome == -1:
            self.match_tuple[1] = self.match_tuple[1] - 1

        self.match_tuple[2] = self.match_tuple[2] + 1

        # update all values for the current node.


    def random_playout (state):
        while state.children != 0:
            random(children)
            state = state.children

        raise NotImplementedError("You must implement this method")

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
        for i in range(playouts):
            node = self
            #selection
            while self.children(expended) and self.legal_moves != 0:
                node = 
            #expansion
            if self.legal_moves != 0:
                for j in self.children:
                    if j notexplored:
                        new_node = MctsNode(self.state.move, self, self.ucb_const)         
                        #simulation
                        outcome = new_node.state.random_playout()
            else:
                outcome = self.state
            #backpropagation
            self.parent.update_play_counts(outcome)

            # wrote the beginning of the four steps, stll need to figure out a way to store the visited nodes.
            # I think im going to use named tuples to store p1_wins, p2_wins and total matches.

            

