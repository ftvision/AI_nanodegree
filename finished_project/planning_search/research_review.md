
# PDDL: the Planning Domain Definition Language

Describes the initial and goal states as conjunctions of literals, and actions in terms of their pre-conditions and effects.

(Ghallab et al, 1998) a computer-parsable, standardized syntax for representing planning problems and has been used as the standard language for the International Planning Competition scince 1998 PDDL 3.0 (Gerevini and Long, 2005)

# GPS, the General Problem Solver (Newell and Simon, 1961)

a state-space search system that used means-ends analysis

# STRIPS (Fikes and NIlsson, 1971)

First major planning system

Bylander(1992), Fikers and Nilsson(1993)-Historical retrospectives

# WARPLAN
One solution to the interleaving problem was goal-regression planning, a technique in
which steps in a totally ordered plan are reordered so as to avoid conflict between subgoals.
This was introduced by Waldinger (1975) and also used by Warren’s (1974) W ARPLAN .
W ARPLAN is also notable in that it was the first planner to be written in a logic program-
ming language (Prolog) and is one of the best examples of the remarkable economy that can
sometimes be gained with logic programming: W ARPLAN is only 100 lines of code, a small
fraction of the size of comparable planners of the time.

# Partial-order planning
Partial-order planning dominated the next 20 years of research, yet the first clear for-
mal exposition was T WEAK (Chapman, 1987), a planner that was simple enough to allow
proofs of completeness and intractability (NP-hardness and undecidability) of various plan-
ning problems

# New planner
FASTD OWNWARD (Helmert, 2006)
is a forward state-space search planner that preprocesses the action schemas into an alter-
native representation which makes some of the constraints more explicit. F AST D OWNWARD
(Helmert and Richter, 2004; Helmert, 2006) won the 2004 planning competition, and LAMA
(Richter and Westphal, 2008), a planner based on F AST D OWNWARD with improved heuris-
tics, won the 2008 competition.

# Situation Calculus
The situation calculus approach to planning was introduced by John McCarthy (1963).
The version we show here was proposed by Ray Reiter (1991, 2001).



# The Action Description Language (ADL, Pednault, 1986) 
- Further by Nebel(2000) explores schemes for comiling ADL into Strips. 


# Surveys

Weld (1994,1999)

Constaint-based approches such as GRAPHPLAN and SATPlan are best for NP-hard domains, while search-based approaches do better in domains where feasible solutions can be found without backtracking. 
