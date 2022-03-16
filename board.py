import os
import numpy as np
from scipy.signal import convolve2d
from termcolor import colored
os.system('color')

horizontal_kernel = np.array([[ 1, 1, 1, 1]])
vertical_kernel = np.transpose(horizontal_kernel)
diag1_kernel = np.eye(4, dtype=np.uint8)
diag2_kernel = np.fliplr(diag1_kernel)
detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]

ROW = 6
COL = 7

class Board():
    # 6 tall 7 wide
    def __init__(self, state) -> None:
        if not np.any(state):
            self.state = np.zeros((ROW, COL), dtype= int)
        else:
            self.state = state
    
    def display(self):
        print("-----------------------------")
        for row in self.state:
            print("| ", end="")
            for col in row:
                if col == 0:
                    print(" ", end=" | ")
                elif col == 1:
                    print(colored('0', 'red'), end=" | ")
                elif col == 2:
                    print(colored('0', 'yellow'), end=" | ")
            print("\n-----------------------------")
    
    def placeTile(self, player, column):
        for row in range(len(self.state) - 1, -1, -1):
            if self.state[row][column] == 0:
                self.state[row][column] = player
                return [row, column]
        return None

    def newState(self, player, column) -> np.ndarray:
        copyBoard = np.copy(self.state)
        for row in range(len(copyBoard) - 1, -1, -1):
            if copyBoard[row][column] == 0:
                copyBoard[row][column] = player
                return copyBoard
        return None

    def isWinner(self, player):
        for kernel in detection_kernels:
            if (convolve2d(self.state == player, kernel, mode="valid") == 4).any():
                return True
        return False

    def clear(self):
        self.state = np.zeros((ROW, COL), dtype= int)
    
    def full(self):
        return not 0 in self.state
    
    def getHeight(self, column):
        for row in range(len(self.state) - 1, -1, -1):
            if self.state[row][column] == 0:
                return row
