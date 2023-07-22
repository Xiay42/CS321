% call can_draw on one above and below the given number
can_draw_plus_or_minus_one(Number, List) :-
	X is Number + 1,
	can_draw(X, List).
can_draw_plus_or_minus_one(Number, List) :-
	X is Number - 1,
	can_draw(X, List).

% can_draw(Number, List) returns true if you can successfully remove Number from List, and if can_draw works out for 
% the list that remains for a number that is one bigger or one smaller than Number.
can_draw(_, List) :- length(List, 0).
can_draw(Number, List) :-
	append(Left, [Number | Right], List),
	append(Left, Right, WithoutNumber),
	can_draw_plus_or_minus_one(Number, WithoutNumber).

% valid_puzzle(List) determines whether or not a supplied list is a valid puzzle. 
valid_puzzle(List) :-
	append(_, [Number | _], List),
	can_draw(Number, List).
