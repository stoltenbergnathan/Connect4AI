from random import randint
from qtable import Qtable 
from board import Board

class RLAgent():
    def __init__(self, table: Qtable, player) -> None:
        self.table = table
        self.player = player
    
    def selectAction(self, state: Board, n) -> int:
        return randint(0, 6)

    def getReward(self, state: Board, action) -> int:
        # 100 for 4 in a row
        updatedState = Board(state.newState(self.player, action))

        if updatedState.isWinner(self.player):
            return 100
        return 0

    def updateTable(self, state, reward, action, newState) -> None:
        currQ = self.table.getValue(state)["actions"]
        nextQ = self.table.getValue(newState)["actions"]

        Qactions = []
        for a in range(7):
            Qactions.append(nextQ[a])
        
        newQ = currQ[action] + 0.2 * (reward + 0.9 * max(Qactions) - currQ[action])
        self.table.setValue(state, action, newQ)