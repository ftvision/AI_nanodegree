# Notes

1. In the `MinimaxPlayer.min_val()`, the evaluation function should be `self.score(game, game.inactive_player)`
  - This is because we ALWAYS evaluate the state from the perspective of the **root-players**
  - we could either always supply a parameter `player` to make sure we always evaluate the state from this player
  - or we can use `game.inactive_player` in the `min_val()` and `game.active_player` in the `max_val()` function  

2. In the `class AlphaBetaPlayer`, the pruning starts from the first `max` level by using `alpha_beta_max_val()`.
  - Similarly, we have the `self.score()` function ALWAYS evaluate the states from the root player's perspective 
