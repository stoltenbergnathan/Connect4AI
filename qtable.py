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
    
    def save(self, filename):
        file = open(filename, "w")
        for line in self.table:
            file.write(f'{line["state"]},{line["actions"][0]},{line["actions"][1]},{line["actions"][2]},{line["actions"][3]},{line["actions"][4]},{line["actions"][5]},{line["actions"][6]}\n')
        file.close()

    def load(self, filename):
        pass