from turtle import st
from board import Board
import numpy as np

class Qtable():
    def __init__(self) -> None:
        self.table = []
    
    def display(self):
        for value in self.table:
            print(value)

    def getValue(self, state):
        for value in self.table:
            if np.array_equal(state, value['state']):
                return value
        return self.initValue(state)

    def setValue(self, state, action, newValue):
        for value in self.table:
            if np.array_equal(state, value['state']):
                value["actions"][action] = newValue
                return
        self.initValue(state)
        self.setValue(state, action, newValue)

    def initValue(self, state):
        self.table.append({"state": state, "actions": [0, 0, 0, 0, 0, 0, 0]})
        return {"state": state, "actions": [0, 0, 0, 0, 0, 0, 0]}

test = Qtable()
test.setValue(Board().state, 1, 999)
test.display()