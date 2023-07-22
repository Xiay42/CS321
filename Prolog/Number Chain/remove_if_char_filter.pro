% --- Remove all characters who violate given rule---
% Goal: replace re.sub(r'[^a-zA-Z0-9 ]', '', s)
%   Visualization: https://regexper.com/#%5B%5Ea-zA-Z0-9%20%5D
% Goal: replace re.sub(r'[^a-zA-Z ]', '', s)
%   Visualization: https://regexper.com/#%5B%5Ea-zA-Z%20%5D
% By Lev Shuster
% 6/8/2023

remove_if([], _, []). % because a empty list don't have to filter, result is an empty list
remove_if([Char | Chars], Filter, Out) :- % if character violates rule, don't include in results
    \+ char_type(Char,Filter),
    remove_if(Chars, Filter, Out).
remove_if([Char | Chars], Filter, Out) :- % if character passes rule, include in result
    char_type(Char,Filter),
    remove_if(Chars, Filter, Result),
    Out = [Char | Result].

string_remove_if(String, Filter, Result) :-
    string_chars(String, Chars),
    remove_if(Chars, Filter, Char_result),
    string_chars(Result, Char_result).

% availible filters: www.swi-prolog.org/pldoc/man?predicate=char_type/2
without_numbers(String, Result) :-
    string_remove_if(String, alpha, Result).
without_special_characters(String, Result) :-
    string_remove_if(String, alnum, Result).
