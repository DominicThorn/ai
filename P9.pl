male(john).
male(mike).
male(david).
male(robert).

female(mary).
female(lisa).
female(susan).
female(emma).

parent(john, mike).
parent(mary, mike).
parent(john, lisa).
parent(mary, lisa).
parent(mike, david).
parent(susan, david).
parent(mike, emma).
parent(susan, emma).

father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
child(X, Y) :- parent(Y, X).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
