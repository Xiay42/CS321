Results:
    itdeep search randomstate with num_moves = 10: 0.011005786657333374
    itdeep search randomstate with num_moves = 15: 0.4635890436172485
    itdeep search randomstate with num_moves = 20: 5.167461528778076

    astar search with num_moves = 10, heuristic = num_wrong_tiles: 0.00020656704902648925
    astar search with num_moves = 15, heuristic = num_wrong_tiles: 0.00042604684829711915
    astar search with num_moves = 20, heuristic = num_wrong_tiles: 0.0012395548820495605
    astar search with num_moves = 50, heuristic = num_wrong_tiles: 0.07605065107345581

    astar search with num_moves = 10, heuristic = manhattan_distance: 0.0003806138038635254
    astar search with num_moves = 15, heuristic = manhattan_distance: 0.0004613113403320313
    astar search with num_moves = 20, heuristic = manhattan_distance: 0.0006626367568969727
    astar search with num_moves = 50, heuristic = manhattan_distance: 0.005956673622131347
    astar search with num_moves = 100, heuristic = manhattan_distance: 0.03647778749465942

    note: for itdeep, there are some cases where it took 100+ secs to finish the search, while others
        only take about less than 1. This is not the case for astar search.

Procedure:
    I timed both search methods 100 times and took the average, varing the num_moves and heuristics in
    the case of astar search.
        pros: it's easier to implement the timing mechanism
        cons: it doesn't guarantee that as the num_moves goes up the complexity (goal state depth) increases,
            but it's a good estimate. 

Analysis:
    Astar search performs much better than itdeep search, although this result depends on which heuristic you use.
    bwtween the two methods I tried, manhattan_distance performs better than num_wrong_tiles.
    This is because Astar search is a form of informed search, and the accuracy of the additional information
    determines how well the search performs in terms of time. It will almost always be better than uninformed search
    because as long as the heuristic is a valid one informed search will always move in closer to the goal in average
    but uninformed search just tries out every possible path to get to the goal, hence the 100+ secs trials.


