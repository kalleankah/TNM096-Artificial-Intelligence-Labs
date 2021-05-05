% STRIPS planner with iterative deepening
% "plan" = if no solution is found at a certain level, the level is increased by 1
% "plan(MaxL)" = works the same as "plan" but with an upper limit MaxL for level.
%                 If no solution is found within MaxL then no solution is found

plan :-
     initial_state(IS),
     goal_state(GS),
     increase(Level),
     write('Level '),Level1 is Level+1,writeNLNL(Level1),
     solve(IS,GS,[],Plan,0,Level),
     printPlan(Plan).


% Planner with a max depth level
plan(MaxL) :-
     initial_state(IS),
     goal_state(GS),
     increase(Level),
     ( Level = MaxL,
       !,
       writeNL('Solution not found')
     ;
       write('Level '),Level1 is Level+1,writeNLNL(Level1),
       solve(IS,GS,[],Plan,0,Level),
       printPlan(Plan)
     ).


% if Goal is a subset of State, then return Plan
solve(State, Goal, Plan, Plan, _, _):-
     is_subset(Goal, State), !.

% otherwise, select next action. increase the counter and move to the next state
solve(State, Goal, Sofar, Plan, Counter, Level):-
     Counter =< Level,
     act(Action, Precons, Delete, Add),
     is_subset(Precons, State),
     % \+ member(Action, Sofar),      NOT needed since we have MAX level. Having it may block the construction of plans that require an action to be repeated twice
     delete_list(Delete, State, Remainder),
     add_list(Add, Remainder, NewState),
     NewCounter is Counter+1,
     solve(NewState, Goal, [Action|Sofar], Plan, NewCounter, Level).




% AUXILIARY

increase(0).
increase(X) :- increase(Y), X is Y+1.

% Check is first list is a subset of the second
is_subset([], _) :- !.
is_subset([diff(A,B)|T], Set):- !, \+ A=B, is_subset(T, Set).
is_subset([H|T], Set):- member(H, Set), is_subset(T, Set).


printPlan(Plan) :-
     length(Plan, Length),
     write('----- A Plan (length '), write(Length), writeNL(')'),
     printPlan2(Plan),
     writeNL('-------------------------').

printPlan2([]) :- !.
printPlan2([H|T]):- printPlan2(T), writeNL(H).

% Remove all elements of 1st list from second to create third.
delete_list([], State, State) :- !.
delete_list([H|T], State, Newstate):-
           remove(H, State, Remainder), delete_list(T, Remainder, Newstate).

add_list(Add, Remainder, NewState) :-  append(Add, Remainder, NewState), !.
           
remove(X, [X|T], T) :- !.
remove(X, [H|T], [H|R]):- remove(X, T, R).

writeNL(X) :- !, write(X), nl.
writeNLNL(X) :- !, write(X), nl, nl.
