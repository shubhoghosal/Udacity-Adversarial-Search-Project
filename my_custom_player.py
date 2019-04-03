
from sample_players import DataPlayer
import random

class CustomPlayer_Random(DataPlayer):

    def get_action(self, state):

        self.queue.put(random.choice(state.actions()))

class CustomPlayer_Minimax(DataPlayer):

    def get_action(self, state):

        print("Entering get action")
        print("State: ", state)
        print("Player: ", self.player_id)
        if state.ply_count <=1:
            print("Adding random choice to self queue")
            self.queue.put(random.choice(state.actions()))
        else:
            print("Adding Minimax choice to self queue")
            self.queue.put(self.minimax(state, depth=2))

    def minimax(self, state, depth):

        def min_value(state, depth):

            print("Entering Min Value")
            print("Player: ", self.player_id)

            if state.terminal_test():
                print("Terminal state reached in Min Value.")
                print("Returning value from Min Value: ", state.utility(self.player_id))
                print("Exiting Min Value.")
                return state.utility(self.player_id)
            if depth <= 0: 
                print("Depth Limit Reached.")
                print("Score: ", self.score(state))
                print("Exiting Min Value.")
                return self.score(state)
            value = float("inf")
            for action in state.actions():
                print("Next Action in Min Value: ", action)
                print("Result: ", state.result(action))
                value = min(value, max_value(state.result(action), depth - 1))

            print("Returning value from Min Value: ", value)
            print("Exiting Min Value")
            return value


        def max_value(state, depth):

            print("Entering Max Value")
            print("Player: ", self.player_id)

            if state.terminal_test():
                print("Terminal state reached in Max Value.")
                print("Returning value from Max Value: ", state.utility(self.player_id))
                print("Exiting Max Value.")
                return state.utility(self.player_id)
            if depth <= 0: 
                print("Depth Limit Reached.")
                print("Score: ", self.score(state))
                print("Exiting Max Value.")
                return self.score(state)
            value = float("-inf")
            for action in state.actions():
                print("Next Action in Max Value: ", action)
                print("Result: ", state.result(action))
                value = max(value, min_value(state.result(action), depth -1))

            print("Returning value from Max Value: ", value)
            print("Exiting Max Value.")
            return value

        print("Entering Minimax")
        print("Player: ", self.player_id)
        best_score = float("-inf")
        best_move = None
        moves = {}
        for action in state.actions():
            print("Next Action in Minimax: ", action)
            print("Result: ", state.result(action))
            value = min_value(state.result(action), depth -1)
            moves.update({action: value})
        max_score = max([score for move, score in moves.items()])
        best_moves = [move for move, score in moves.items() if score == max_score]
        print("Best Moves: ", best_moves)
        print("Exiting Minimax")
        return max(best_moves)

    def score(self, state):
        current_player_loc = state.locs[self.player_id]
        opponent_player_loc = state.locs[1 - self.player_id]
        current_player_liberties = state.liberties(current_player_loc)
        opponent_player_liberties = state.liberties(opponent_player_loc)
        return len(current_player_liberties) - len(opponent_player_liberties)

CustomPlayer = CustomPlayer_Minimax