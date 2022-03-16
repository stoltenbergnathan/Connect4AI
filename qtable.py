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

    def newQState(self, state, actions):
        self.table.append({"state": state, "actions": actions})
    
    def combineQ(self, state, actions):
        for value in self.table:
            if np.array_equal(state, value['state']):
                # Merge values
                for count, action in enumerate(value["actions"]):
                    value["actions"][count] = max(action, actions[count])
                return
        self.newQState(state, actions)
    
    def save(self, filename):
        file = open(filename, "w")
        for line in self.table:
            file.write(f'{line["state"]},{line["actions"][0]},{line["actions"][1]},{line["actions"][2]},{line["actions"][3]},{line["actions"][4]},{line["actions"][5]},{line["actions"][6]}\n')
        file.close()

    def load(self, filename):
        file = open(filename, "r")
        while True:
            line = file.readline().rstrip()
            if not line:
                break
            values = line.split(']')
            state = []
            rewards = []
            for value in values[0].replace('[', '').split(','):
                state.append(int(value))
            for value in values[1].removeprefix(',').split(','):
                rewards.append(float(value))        
            self.newQState(state, rewards)
        file.close()

    def combine(self, file1, file2, outfile):
        file1 = open(file1, "r")
        file2 = open(file2, "r")
        while True:
            line = file1.readline().rstrip()
            if not line:
                break
            values = line.split(']')
            state = []
            rewards = []
            for value in values[0].replace('[', '').split(','):
                state.append(int(value))
            for value in values[1].removeprefix(',').split(','):
                rewards.append(float(value))
            self.combineQ(state, rewards)
        file1.close()
        while True:
            line = file2.readline().rstrip()
            if not line:
                break
            values = line.split(']')
            state = []
            rewards = []
            for value in values[0].replace('[', '').split(','):
                state.append(int(value))
            for value in values[1].removeprefix(',').split(','):
                rewards.append(float(value))
            self.combineQ(state, rewards)
        file2.close()
        self.save(outfile)
