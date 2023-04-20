import puzzle8 as p8
import heapq
from typing import List
import time

goal_position = [(1, 1), (0, 0), (1, 0),
                 (2, 0), (2, 1), (2, 2),
                 (1, 2), (0, 2), (0, 1)]

def num_wrong_tiles(state) -> int:
    """Given a puzzle, returns the number of tiles that are in the wrong
    location. Does not count the blank space.
    """
    count = 0
    for i in range(9):
        if p8.get_tile(state, i) != p8.get_tile(p8._goal,i) and p8.get_tile(state, i) != 0:
            count += 1
    return count

def manhattan_distance(state) -> int:
    """Given a puzzle, returns the Manhattan distance to the solution state.
    Does not count the distance from blank space to its correct location as
    part of the distance.
    """
    dist=0
    for num in range(1,9):
        for square in range(9):
            if p8.get_tile(state,square) == num:
                position = p8.xy_location(square)
                # print (num, position)
                dist += abs(position[0] - goal_position[num][0]) + abs(position[1] - goal_position[num][1])
    return dist

def astar_search(state: int, heuristic) -> List[int]:
    """Finds path to solution via A* search, using the provided heuristic.
    Returns a list of squares that the blank moves to in order to get to
    solution.
    """
    h = []
    v = []
    d = {}
    node = 0
    if state == p8._goal:
        return state
    else:
        heapq.heappush(h, (heuristic(state), state))
        v.append(state)
        while p8._goal not in v:
            node = heapq.heappop(h)[1] 
            neighbors = p8.neighbors(p8.blank_square(node))
            for n in neighbors:
                next_state = p8.move_blank(node, n)
                if next_state not in v:
                    v.append(next_state)
                    d[next_state] = node
                    heapq.heappush(h, (heuristic(next_state) + len(get_path(state, next_state, d)), next_state))
        p = get_path(state, p8._goal, d)
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
            print("num of wrong tile: ",num_wrong_tiles(i))
            print()




def main():
    # puzzle = p8.state([0,2,3,6,7,8,1,5,4])
	t_time = 0
	trials = 100
	for i in range(trials):
		puzzle = p8.random_state(num_moves=50)
		start = time.time()
		astar_search(puzzle, num_wrong_tiles)
		end = time.time()
		time_for_one = end - start
		print(time_for_one)
		t_time += time_for_one
	avg_time = t_time/trials
	print (avg_time)

if __name__ == "__main__":
	main()