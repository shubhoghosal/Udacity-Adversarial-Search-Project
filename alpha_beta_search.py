def alpha_beta_search(gameState, player_id, depth):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    alpha = float("-inf")
    beta = float("inf")
    best_score = float("-inf")
    best_move = None
    for a in gameState.actions():
        v = min_value(gameState.result(a), alpha, beta, depth)
        alpha = max(alpha, v)
        if v > best_score:
            best_score = v
            best_move = a
    return best_move

# TODO: modify the function signature to accept an alpha and beta parameter
def min_value(gameState, alpha, beta, depth):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)
    
    if depth <= 0:
        return score(gameState) #my_moves(gameState)

    v = float("inf")
    for a in gameState.actions():
        # TODO: modify the call to max_value()
        v = min(v, max_value(gameState.result(a), alpha, beta, depth))
        # TODO: update the value bound
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

# TODO: modify the function signature to accept an alpha and beta parameter
def max_value(gameState, alpha, beta, depth):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)
    
    if depth <= 0:
        return score(gameState) #my_moves(gameState)
    
    v = float("-inf")
    for a in gameState.actions():
        # TODO: modify the call to min_value()
        v = max(v, min_value(gameState.result(a), alpha, beta, depth))
        # TODO: update the value bound
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def my_moves(gameState):
    loc = gameState.locs[player_id]
    return len(gameState.liberties(loc))

def score(self, state):
    own_loc = state.locs[self.player_id]
    opp_loc = state.locs[1 - self.player_id]
    own_liberties = state.liberties(own_loc)
    opp_liberties = state.liberties(opp_loc)
    return len(own_liberties) - len(opp_liberties)
