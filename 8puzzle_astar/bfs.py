# written by Michael Xia
# 3.30.2023



import puzzle8 as p8
from typing import List
from collections import deque


def breadth_first_search(state: int) -> List[int]:
    """Finds path to solution via breadth-first search. Returns a list of
    squares that the blank moves to in order to get to solution.
    """
    # q is the prioity queue to impliment the tree structure
    # v is a list the keeps track of the states that's been visited
    # d is a dictionary that keeps track of the parent of each node
    # node is a node in the tree
    q = deque('')
    v = []
    d = {}
    node = 0
    # check if the start state is the goal
    if state == p8._goal:
        return state
    else:
        root = state
        q.append(root)
        v.append(root)
        # this while loop stops when we are one step away from goal
        while p8._goal not in q:
            node = q.popleft()
            neighbors = p8.neighbors(p8.blank_square(node))
            for n in neighbors:
                next_state = p8.move_blank(node, n)
                # check if this state has been visited
                if next_state not in v:
                    # if not, enqueue, mark as visited and remember the parent of this state.
                    q.append(next_state)
                    v.append(next_state)
                    d[next_state] = node
        p = get_path(state, p8._goal, d)
        # display_path(p)
    return p



def get_path(start, goal, dict):
    # check to see if we actually have a solution
    if goal not in dict:
        return None
    else:
        l = []
        state = goal
        # start from the goal state and add it's parent, the parent of the parent and so on to a list
        # until we reach the start state
        while state != start:
            l.append(state)
            state = dict[state]
    l.reverse()
    return l

def display_path(p):
    if p == None:
        print("no solution")
    else:
        for i in p:
            p8.display(i)
            print()

 
r_state = p8.random_state()
p8.display(r_state)

breadth_first_search(r_state)

