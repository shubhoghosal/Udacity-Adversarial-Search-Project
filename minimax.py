
def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    # TODO: Finish this function!
    print("Entering Minimax")
    print("Player: ", gameState.player())
    best_score = float("-inf")
    best_move = None
    moves = {}
    for a in gameState.actions():
        print("Action: ", a)
        print("Result: ", gameState.result(a))
        v = min_value(gameState.result(a))
        moves.update({a: v})
    max_score = max([score for move, score in moves.items()])
    best_moves = [move for move, score in moves.items() if score == max_score]
    print("Best Moves: ", best_moves)
    return max(best_moves)

def min_value(gameState):
    """ Return the game state utility if the game is over,
    otherwise return the minimum value over all legal successors
    """
    print("Entering Min Value")
    print("Player: ", gameState.player())
    
    if gameState.terminal_test():
        print("Terminal state reached in min-value.")
        print("Returning value from min-value: ", gameState.utility(gameState.player()))
        return gameState.utility(gameState.player())
    v = float("inf")
    for a in gameState.actions():
        print("Action: ", a)
        print("Result: ", gameState.result(a))
        v = min(v, max_value(gameState.result(a)))
        print("Came out of min-value")

    print("Returning value from min-value: ", v)
    return v


def max_value(gameState):
    """ Return the game state utility if the game is over,
    otherwise return the maximum value over all legal successors
    """
    print("Entering Max Value")
    print("Player: ", gameState.player())

    if gameState.terminal_test():
        print("Terminal state reached in max-value.")
        print("Returning value from max-value: ", gameState.utility(gameState.player()))
        return gameState.utility(gameState.player())
    v = float("-inf")
    for a in gameState.actions():
        print("Action: ", a)
        print("Result: ", gameState.result(a))
        v = max(v, min_value(gameState.result(a)))
        print("Came out of max-value")

    print("Returning value from max-value: ", v)
    return v