load set operations library
:- use_module(library(lists)).

start :-
    write('Choose: math / set'), nl,
    read(Type),
    run(Type).

% --- Simple Math ---
run(math) :-
    write('Enter X: '), read(X),
    write('Enter Y: '), read(Y),
    write('Op (add, subtract, multiply, divide): '), read(Op),
    math_calc(Op, X, Y, R),
    write('Result: '), write(R), nl.

math_calc(add, X, Y, R)      :- R is X + Y.
math_calc(subtract, X, Y, R) :- R is X - Y.
math_calc(multiply, X, Y, R) :- R is X * Y.
math_calc(divide, X, Y, R)   :- R is X / Y.

% --- Simple Sets ---
run(set) :-
    write('Enter Set1 (e.g. [1,2]): '), read(S1),
    write('Enter Set2 (e.g. [2,3]): '), read(S2),
    write('Op (union, intersection, difference): '), read(Op),
    set_calc(Op, S1, S2, R),
    write('Result: '), write(R), nl.

set_calc(union, S1, S2, R)        :- union(S1, S2, R).
set_calc(intersection, S1, S2, R) :- intersection(S1, S2, R).
set_calc(difference, S1, S2, R)   :- subtract(S1, S2, R).


:- dynamic pizza/3.
start :-
    menu.

menu :-
    nl,
    write('1. Add Pizza'), nl,
    write('2. Order Pizza'), nl,
    write('3. Display Menu'), nl,
    write('4. Exit'), nl,
    write('Enter your choice: '),
    read(Choice),
    process(Choice).

process(1) :- add_pizza, menu.
process(2) :- order_pizza, menu.
process(3) :- display_menu, menu.
process(4) :- write('Thank you!'), nl.
process(_) :- write('Invalid choice'), nl, menu.

add_pizza :-
    write('Enter pizza name: '), nl,
    read(Name),
    write('Enter price: '), nl,
    read(Price),
    write('Enter quantity available: '), nl,
    read(Qty),
    assertz(pizza(Name, Price, Qty)),
    write('Pizza added successfully!'), nl.

display_menu :-
    write('Available Pizzas:'), nl,
    forall(pizza(Name, Price, Qty),
        (write(Name), write(' - Rs.'), write(Price),
         write(' - Qty: '), write(Qty), nl)
    ).

order_pizza :-
    write('Enter number of pizzas to order: '), nl,
    read(N),
    take_orders(N, Total),
    write('Total Bill = Rs.'), write(Total), nl.

take_orders(0, 0).
take_orders(N, Total) :-
    N > 0,
    write('Enter pizza name: '), nl,
    read(Name),
    write('Enter quantity: '), nl,
    read(Qty),

    ( pizza(Name, Price, AvailableQty) ->
        ( Qty =< AvailableQty ->
            Subtotal is Price * Qty,
            write('Subtotal = Rs.'), write(Subtotal), nl,

            NewQty is AvailableQty - Qty,
            retract(pizza(Name, Price, AvailableQty)),
            assertz(pizza(Name, Price, NewQty)),

            N1 is N - 1,
            take_orders(N1, RestTotal),
            Total is Subtotal + RestTotal
        ;
            write('Not enough pizza quantity available!'), nl,
            take_orders(N, Total)
        )
    ;
        write('Pizza not found!'), nl,
        take_orders(N, Total)
    ).


male(marthanda_varma).
male(ravi_varma).
male(dharma_raja).
male(balarama_varma).
male(rajaraja_varma).
male(swathi_thirunal).
male(uthram_thirunal).
male(ayilyam_thirunal).
male(visakham_thirunal).
male(sree_moolam_thirunal).
male(chithira_thirunal).
male(uthradom_thirunal).
male(balagopal_varma).
male(moolam_thirunal_rama_varma).
male(ananthapadmanabhan).
male(consort1).
male(consort2).
male(consort3).
male(prince_test).

female(karthika_thirunal).
female(pooruruttathi_thirunal).
female(gowri_lakshmi_bayi).
female(gowri_parvati_bayi).
female(princess_zed).
female(sethu_lakshmi_bayi).
female(sethu_parvathi_bayi).
female(lalithamba_bayi).
female(indira_bayi).
female(karthika_bayi).
female(rukmini_bayi).
female(parvati_devi).
female(queen1).
female(queen2).
female(queen3).

married(ragava_varma, karthika_thirunal).
married(pooruruttathi_thirunal, ravi_varma).
married(marthanda_varma, queen1).
married(dharma_raja, queen2).
married(balarama_varma, queen3).
married(rajaraja_varma, gowri_lakshmi_bayi).
married(sethu_lakshmi_bayi, consort3).
married(chithira_thirunal, sethu_parvathi_bayi).

spouse(X,Y) :- married(X,Y).
spouse(X,Y) :- married(Y,X).

parent(ragava_varma, marthanda_varma).
parent(ragava_varma, pooruruttathi_thirunal).
parent(karthika_thirunal, marthanda_varma).
parent(karthika_thirunal, pooruruttathi_thirunal).
parent(pooruruttathi_thirunal, dharma_raja).
parent(ravi_varma, dharma_raja).
parent(dharma_raja, balarama_varma).

parent(balarama_varma, gowri_lakshmi_bayi).
parent(balarama_varma, gowri_parvati_bayi).

parent(gowri_lakshmi_bayi, swathi_thirunal).
parent(gowri_lakshmi_bayi, uthram_thirunal).
parent(gowri_lakshmi_bayi, princess_zed).
parent(rajaraja_varma, swathi_thirunal).
parent(rajaraja_varma, uthram_thirunal).
parent(rajaraja_varma, princess_zed).

parent(princess_zed, ayilyam_thirunal).
parent(princess_zed, visakham_thirunal).
parent(princess_zed, sree_moolam_thirunal).

parent(sree_moolam_thirunal, sethu_lakshmi_bayi).
parent(sree_moolam_thirunal, sethu_parvathi_bayi).

parent(sethu_lakshmi_bayi, lalithamba_bayi).
parent(sethu_lakshmi_bayi, indira_bayi).
parent(lalithamba_bayi, balagopal_varma).
parent(lalithamba_bayi, ruralni_bayi).

parent(sethu_parvathi_bayi, chithira_thirunal).
parent(sethu_parvathi_bayi, karthika_bayi).
parent(sethu_parvathi_bayi, uthradom_thirunal).

parent(karthika_bayi, moolam_thirunal_rama_varma).
parent(uthradom_thirunal, ananthapadmanabhan).
parent(uthradom_thirunal, parvati_devi).
parent(swathi_thirunal, prince_test).

father(F,C) :- parent(F,C), male(F).
mother(M,C) :- parent(M,C), female(M).

child(C,P) :- parent(P,C).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

siblings(X, Siblings) :-
    setof(Y, P^(parent(P, X), parent(P, Y), X \= Y), Siblings).

brother(B,X) :- sibling(B,X), male(B).
sister(S,X) :- sibling(S,X), female(S).

cousin(X,Y) :-
    parent(P1,X),
    parent(P2,Y),
    sibling(P1,P2),
    X \= Y.

ancestor(A,D) :- parent(A,D).
ancestor(A,D) :-
    parent(A,X),
    ancestor(X,D).

father_in_law(F,X) :-
    spouse(X,S),
    father(F,S).

mother_in_law(M,X) :-
    spouse(X,S),
    mother(M,S).

brother_in_law(BIL, X) :-
    sibling(X, S), spouse(S, BIL), male(BIL).
brother_in_law(BIL, X) :-
    spouse(X, S), brother(BIL, S).

sister_in_law(SIL, X) :-
    sibling(X, S), spouse(S, SIL), female(SIL).
sister_in_law(SIL, X) :-
    spouse(X, S), sister(SIL, S).

