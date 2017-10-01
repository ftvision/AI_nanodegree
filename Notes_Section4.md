# Section 4

This section covers the following topics on **Reasoning** and **Planning**:

- Propositional Logic
- First Order Logic
- Classical Planning
- Forward/Backward State Space search
- Situation Calculus

## Reference

## Logic Reasoning: Background and Expert Systems

- Logic -> Probability
- Hand-made feature -> machine learning

## Propositional Logic

```
(E or B) > A
A > (J and M)
J == M
```

- Propositional logic is either `True` or `False` w.r.t. a model of the world
- use **Truth Table** to decide the results of a proposition
- Limitations:
    - can only handle `True` or `False`, no uncertainty
    - cannot talk about objects
    - there are no short cuts

## Terminology

- Valid
    - `True` in every possible model
- Satisfiable
    - `True` in some models, but not in others
- UnSatisfiable
    - `False` in all models

## Representations

- Logic model about the world:
    - ontological commitment of these logics
    - **first order logic**: relations, functions, objects
    - **Propositional logic**: facts
    - **Probability theory**: facts
- Beliefs that agent can have by using these logics:
    - epistemological commitments
    - **first order logic**: True, False, Unknown
    - **propositional logic**: True, False, Unknown
    - **probability theory**: real number [0,1]

- Representations from another perspective
    - **Atomic representation**: a representation of the state is just an individual state when no piece is inside of it.
        - search, problem solving
        - no internal structure in the state
    - **Factored representation**: a representation of the world is factored into several variables
        - variables
    - **Structured representation**: a representation that includes relationships between objects, a branching structure, complex representations
        - traditional programming languages
        - database

## First Order Logic

- Logic relations are on objects, but not on relations
- Higher order logic: relations can be among relations

### Model

- we start with a set of objects: A1, B2, ....
- we also have a set of constants -- refer to objects, {A, B, C, D, 1, 2, 3} (symbols)
- we also have a set of functions -- **mapping** from objects to objects (e.g. def number_of())
- we also have a set of relations -- ABOVE {[A,B], [C, D]}(binary relation) | VOWEL {[A]} (unary relation)

### Syntax

- sentences, predicates corresponding to relations:
    - `2 == 2`
    - `Vowel(A)`
    - `and, or, imply, ...`
- terms:
    - constants
    - variables
    - functions: number of (A)
    - quantifier:
      - `for all`: $\forall$
      - `there exists`: $\exists$
      - e.g. $\forall x$ `Vowel(x)`
- sentences -- definition
    - a good definition should include `True` scenarios and exclude `False` scenarios
    - cannot leave scenarios undefined

## Planning

We cannot plan everything beforehand. We need some feedback during our execution, so we need to **interleave planning and executing**.

- Environment is stochastic
    - we need to deal with contingencies
- Environment is multi-agent
    - can only update at execution time
- Environment is partial observable
    - partial observability
- Signal is Unknown or Hierarchical
    - planning at high-level, execution at low-level

## State Space

we can derive **belief state space** from our action, even though we don't know the **actual state space**

- **conformant plan**: we form a plan that reaches a goal without ever observing the world.
- partially observable planing:
    - can see what location it is in
    - can see what is going on in the current location
    - take an observation after an action -- reduce the possible numbers of states
- stochastic environment:
    - e.g. state transition is stochastic
- infinite sequences of planning
    - add a loop (a choice-option node) in the state transition tree
- A successful plan
    - we can find a successful plan by **using search!**

## A Mathematical Notation (First order logic description)

say a sequence of states: `[A, S, F]`

- plan in deterministic environment: `Result(Result(A, A->S), S-F) <- Goals`
    - current state, and apply an action from `A -> S`, get an intermediate state
    - continue applying an action from `S -> F`, and see whether the final state is in the `Goals`
- plan in stochastic (partially observable] environment: `b_i` stands for a **belief state**
    - `b' = Update(Predict(b, a), o)`, where `b` is the current state, `a` is the action, and `o` is the observation.

## Classical Planning

- state space:  all the possible assignments --> `k`-boolean ($2^k$ possible states)
- world state: complete assignment of `True` or `False`
- belief state:
    - Complete assignment of `True` or `False`
    - Partial assignment
    - Arbitrary Formula
- action schema:
    - e.g.
        - (Action(Fly(p, x, y))
        - precondition: Plane(p) AND Airport(x) AND Airport(y) AND AT(p,x)
        - effect: NOT AT(p, x) and AT(p, y))
    - similar to First Order Logic, but is just a **Schema**
- **we can derive heuristics by relaxing (pre)conditions in action schema**

## Progression and Regression Search

- Forward Progression State Space Search
  - start at INIT state
  - branching on possible actions -- to another state
  - continue search
  - we have to branching all possible actions
- Backward Regression State Space Search
  - start at GOAL state
  - branching: what action can lead to the current state (look at action schema)
  - continue search backwards (we always have some part of the states unknown)
  - sometimes, with one goal, we only need to backward branch an single action
- Plan Space Search: search through the space of plans
  - start with a single PLAN
  - add one operator into the current PLAN
  - branching the current PLAN on different operators, and make the PLAN richer and richer
  - until we get a successful plan
  - not very popular now

## Situation Calculus (First Order Logic (FOL))

- Actions:
    - objects `Fly(p, x, y)`
- Situations:
    - objects `S0`, `s' = Result(s,a)`
    - Possible actions: `Poss(a, s)`
    - Possible actions is specified by some preconditions: `SomePreCond(s) -> Poss(a,s)`
    - e.g. `Plane(p,s) AND Airport(x,s) AND Airport(y,s) AND At(p, x, s) -> Poss(Fly(p,x,y),s)`
- Fluents (e.g.`At(p, x, s)`) are predicates that can change
- Successor-State Axioms:
    - `FORALL a, s, Poss(a, s) -> (fluent true IFF a made it true OR a didn't undo)`
    - `Poss(a, s) -> In(c,p,result(s,a)) IFF (a = Load(c, p, x) OR (In(c, p, s) AND a != Unload(c, p, x)))`

Once we've described this in the ordinary language of first order logic, we don't need any special programs to manipulate it and come up with the solution，because we already have theorem provers for first order logic.

Apply the normal theorem prover that we already had for other uses, it can come up with an answer of a path that satisfies this goal. That is a situation which corresponds to a path which satisfies this, given the initial state and given the descriptions of the actions.

- Advantage of situation calculus:
  - we have the full power of first order logic
  - we can represent anything we want
  - have much more flexibility
- Weakness
  - we won't be able to distinguish probable and improbable situations.
