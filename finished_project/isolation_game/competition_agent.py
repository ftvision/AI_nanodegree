"""Implement your own custom search agent using any combination of techniques
you choose.  This agent will compete against other students (and past
champions) in a tournament.

         COMPLETING AND SUBMITTING A COMPETITION AGENT IS OPTIONAL
"""
import random
from collections import deque

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def valid_moves_k_ahead(game, loc, step_k):
    """Calculate available moves in next step_k steps"""

    visited = set()
    queue = deque()
    queue.append((0, loc[0], loc[1]))
    visited.add((loc[0], loc[1]))
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
              (1, -2), (1, 2), (2, -1), (2, 1)]

    while queue:
        step, r, c = queue.popleft()
        if step >= step_k:
            break
        valid_moves = [(r + dr, c + dc) for dr, dc in directions
                       if game.move_is_legal((r + dr, c + dc)) and (r + dr, c + dc) not in visited]
        queue.extend([(step + 1, r, c) for r, c in valid_moves])
        visited.update(valid_moves)
    return len(visited)

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    forward_step_k = 3 #calculate the scope of next k steps

    loc_player = game.get_player_location(player)
    if loc_player is None:
        n_player = len(game.get_blank_spaces())
    else:
        n_player = valid_moves_k_ahead(game, loc_player, forward_step_k)

    loc_opponent = game.get_player_location(game.get_opponent(player))
    if loc_opponent is None:
        n_opponent = len(game.get_blank_spaces())
    else:
        n_opponent = valid_moves_k_ahead(game, loc_opponent, forward_step_k)
    return float(n_player - n_opponent)

class CustomPlayer:
    """Game-playing agent to use in the optional player vs player Isolation
    competition.

    You must at least implement the get_move() method and a search function
    to complete this class, but you may use any of the techniques discussed
    in lecture or elsewhere on the web -- opening books, MCTS, etc.

    **************************************************************************
          THIS CLASS IS OPTIONAL -- IT IS ONLY USED IN THE ISOLATION PvP
        COMPETITION.  IT IS NOT REQUIRED FOR THE ISOLATION PROJECT REVIEW.
    **************************************************************************

    Parameters
    ----------
    data : string
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted.  Note that
        the PvP competition uses more accurate timers that are not cross-
        platform compatible, so a limit of 1ms (vs 10ms for the other classes)
        is generally sufficient.
    """

    def __init__(self, data=None, timeout=1.):
        self.score = custom_score
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            depth = 0
            while True:
                depth += 1
                best_move = self.alphabeta(game, depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Implement alpha-beta-pruning
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)

        _, move = self.alpha_beta_max_val(game, depth, alpha, beta)
        return move

    def alpha_beta_max_val(self, game, depth, alpha, beta):
        """Implement Alpha-beta pruning, Max-value-level search

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        int
            Maximum Score of the all legal moves
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if not legal_moves or depth == 0:
            return self.score(game, game.active_player), best_move
        best_value = float("-inf")
        for move in legal_moves:
            value, _ = self.alpha_beta_min_val(game.forecast_move(move), depth - 1, alpha, beta)
            if value > best_value:
                best_value, best_move = value, move
            if best_value >= beta:
                return best_value, best_move
            alpha = max(alpha, best_value)
        return best_value, best_move

    def alpha_beta_min_val(self, game, depth, alpha, beta):
        """Implement Alpha-beta pruning, Min-value-level search

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        int
            Minimum Score of the all legal moves
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if not legal_moves or depth == 0:
            return self.score(game, game.inactive_player), best_move

        best_value = float("inf")
        for move in legal_moves:
            value, val_move = self.alpha_beta_max_val(game.forecast_move(move), depth - 1, alpha, beta)
            if value < best_value:
                best_value, best_move = value, move
            if best_value <= alpha:
                return best_value, best_move
            beta = min(beta, best_value)
        return best_value, best_move
