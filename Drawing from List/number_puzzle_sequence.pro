% draw_plus_or_minus_one() calls draw on one above and below the given number
draw_plus_or_minus_one(Number, List, Result) :-
	X is Number + 1,
	draw(X, List, Result).
draw_plus_or_minus_one(Number, List, Result) :-
	X is Number - 1,
	draw(X, List, Result).

% draw(Number, List) returns list of valid moves to remove all items given a starting position
draw(_, List, []) :- length(List, 0).
draw(Number, List, Result) :-
	append(Left, [Number | Right], List),
	append(Left, Right, WithoutNumber),
	draw_plus_or_minus_one(Number, WithoutNumber, RecursiveResult),
	Result = [Number | RecursiveResult].

% valid_puzzle(List, Sequence) fills in the variable Sequence with a list of numbers that, when removed in that order, 
% correctly solves the problem.
valid_puzzle(List, Sequence) :-
	append(_, [Number | _], List),
	draw(Number, List, Sequence).
