from random import choice, randint
from qtable import Qtable 
from board import Board
import numpy as np
from state import State

class RLAgent():
    def __init__(self, table: Qtable, player) -> None:
        self.table = table
        self.player = player
    
    def selectAction(self, state, n) -> int:
        if randint(0, 100) <= n:
            return randint(0, 6)
        currQ = self.table.getValue(state.state)["actions"]
        best = -111111
        bestOptions = []
        for i in range(7):
            if currQ[i] >= best:
                if currQ[i] > best:
                    bestOptions.clear()
                    best = currQ[i]
                bestOptions.append(i)
        return choice(bestOptions)

    def getReward(self, state: State) -> int:
        # 100 for 4 in a row
        # opponent = 2 if self.player == 1 else 1

        if state.winner():
            return 100
        return 0

    def updateTable(self, state, reward, action, newState) -> None:
        currQ = self.table.getValue(state.state)["actions"]
        nextQ = self.table.getValue(newState.state)["actions"]

        Qactions = []
        for a in range(7):
            Qactions.append(nextQ[a])
        
        newQ = currQ[action] + 0.2 * (reward + 0.9 * max(Qactions) - currQ[action])
        self.table.setValue(state.state, action, newQ)
    
    def play(self, board: Board) -> int:
        nextBoard = None
        state = State(board, self.player)
        while not np.any(nextBoard):
            pickedAction = self.selectAction(state, 10)
            nextBoard = board.newState(1, pickedAction)
        nextState = State(nextBoard, self.player)
        reward = self.getReward(nextState)
        self.updateTable(state, reward, pickedAction, nextState)
        return pickedAction