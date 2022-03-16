from os import stat
from re import T
import numpy as np
from board import Board

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
    
    def save(self, filename):
        file = open(filename, "w")
        for line in self.table:
            flattenedBoard = line["state"].flatten()
            flattenedBoard = np.array2string(flattenedBoard).replace("\n", "")
            file.write(f'{flattenedBoard}, {line["actions"][0]}, {line["actions"][1]}, {line["actions"][2]}, {line["actions"][3]}, {line["actions"][4]}, {line["actions"][5]}, {line["actions"][6]}\n')
        file.close()
    
    def storeValues(self, state, values):
        self.table.append({"state": state, "actions": [values[0], values[1], values[2], values[3], values[4], values[5], values[6]]})

    def load(self, filename):
        file = open(filename, "r")
        while True:
            line = file.readline().rstrip()
            if not line:
                break
            values = line.split(", ")
            flatstr = values[0].replace("[", "").replace("]", "")
            flat = np.fromstring(flatstr, dtype=int, sep=" ")
            state = np.reshape(flat, (6, 7))
            self.storeValues(state, [float(values[1]), float(values[2]), float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7])])