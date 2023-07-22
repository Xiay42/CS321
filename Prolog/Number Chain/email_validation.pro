% --- Email Validator ---
% Goal: replace the following regex statement: ^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$
% Visualization: https://regexper.com/#%5E%5Ba-zA-Z0-9.!%23%24%25%26'*%2B%2F%3D%3F%5E_%60%7B%7C%7D~-%5D%2B%40%5Ba-zA-Z0-9-%5D%2B%28%3F%3A%5C.%5Ba-zA-Z0-9-%5D%2B%29*%24
% By Lev Shuster
% 6/7/2023


% domain letters make up '@gmail.com' or '@ghx.com' or '@carleton.edu' not including the '@' or '.'
is_valid_domain_letter(Char) :-
    char_type(Char,alnum).

is_valid_domain_letter(Char) :-
    Char = '-'.

% A valid URL ensures there are one or more periods and each period is followed by one or more domain letters
% list("gmail.com") => True
% list("gmail.") => False
% list("yahoo.co.uk") => True

is_valid_url_helper(Char) :-
    Char = [].

is_valid_url_helper([Char | Chars]) :-
    is_valid_domain_letter(Char),
    is_valid_url_helper(Chars).

is_valid_url_helper([Char | Chars]) :-
    Char = '.',
    [First | _] = Chars,
    First \= [],
    is_valid_url_helper(Chars).

is_valid_url_helper(Char) :-
    \+ is_list(Char),
    is_valid_domain_letter(Char).

is_valid_url(Chars) :-
    member('.', Chars),
    is_valid_url_helper(Chars).

% An valid email character is any character that can precede the '@' in an email

is_valid_email_char(Char) :-
    is_valid_domain_letter(Char).

is_valid_email_char(Char) :-
    member(Char, ['.', '!', '#', '$', '%', '&', "'", '*', '+', '/', '=', '?', '^', '_', '`', '{', '|', '}', '~', '-']).

% a valid email is a string composed of one or more valid email character followed  by an '@' then a valid url

is_valid_email([Char | Chars]) :-
    is_valid_email_char(Char),
    is_valid_email(Chars).

is_valid_email([Char | Chars]) :-
    Char = '@',
    [First | _] = Chars,
    First \= '.',
    is_valid_url(Chars).

string_is_valid_email(String) :-
    string_chars(String, Chars),
    [First | _] = Chars,
    First \= '@',
    is_valid_email(Chars).