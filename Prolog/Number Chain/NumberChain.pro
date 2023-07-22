% SET THE BOARD

% Replace the following init statments.

init(1,1,13).
init(1,5,27).
init(1,9,39).
init(2,2,11).
init(2,5,24).
init(2,8,37).
init(5,1,71).
init(5,2,70).
init(5,8,34).
init(5,9,43).
init(8,2,81).
init(8,5,62).
init(8,8,53).
init(9,1,79).
init(9,5,63).
init(9,9,51).

% Alteritivly, comment out the init statments and specify init in the IDE

% SET THE GRID SIZE

gridSize(9). % gridSize(9) means that the program should solve on a 9 x 9 grid

% HOW TO CALL FUNCTION

% ['NumberChain.pro'].
% solve(Finished).

% HELPER FUNCTIONS

show(Soln) :-
	reverse(Soln, Forwards),
	write('\n'),
	member(Row, [1,2,3,4,5,6,7,8,9]),
	write('\n'),
	member(Col, [1,2,3,4,5,6,7,8,9]),
	nth1(Value, Forwards, [Row, Col]),
	write(Value),
	write('\t'),
	fail.

gridMax(Result) :-
	gridSize(X),
	Result is X * X.

adjacent(I, J, X, Y) :-
	X is I+1,
	gridSize(Max),
	X =< Max,
	Y is J.
adjacent(I, J, X, Y) :-
	X is I,
	Y is J+1,
	gridSize(Max),
	Y =< Max.
adjacent(I, J, X, Y) :-
	X is I-1,
	X > 0,
	Y is J.
adjacent(I, J, X, Y) :-
	X is I,
	Y is J-1,
	Y > 0.

% PART ONE

complete(Partial, Partial) :-
	length(Partial, Len),
	gridMax(Max),
	Len =:= Max,
	show(Partial). 
	
complete(Partial,Finished) :-
	nth0(0,Partial,LeftMost),
	nth0(0,LeftMost,I),
	nth0(1, LeftMost, J),
	adjacent(I, J, X, Y),
	not(member([X, Y], Partial)),
	init(X, Y, Value),
	length(Partial, PartialLength),
	Value =:= PartialLength + 1,
	append([[X, Y]], Partial, NewPartial),
	complete(NewPartial,Finished).

complete(Partial,Finished) :-
	nth0(0,Partial,LeftMost),
	nth0(0,LeftMost,I),
	nth0(1, LeftMost, J),
	adjacent(I, J, X, Y),
	not(member([X, Y], Partial)),
	not(init(X, Y, _)),
	length(Partial, PartialLength),
	Value is PartialLength + 1,
	not(init(_, _, Value)),
	append([[X, Y]], Partial, NewPartial),
	complete(NewPartial,Finished).

% PART TWO

solve(Final) :-
	init(X, Y, 1),
	!,
	complete([[X, Y]], Final).

solve(Final) :-
	gridSize(Max),
	between(1, Max, X),
	between(1, Max, Y),
	complete([[X, Y]], Final).
