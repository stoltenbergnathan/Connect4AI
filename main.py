import sys
import signal
import numpy as np
from qtable import Qtable
from board import Board
from rlagent import RLAgent
from minMax import MinMax

gameBoard = Board(None)

# Training
# Qtable1 = Qtable()
# Qtable2 = Qtable()
# Qtable1.load("table/savedQ1.txt")
# Qtable2.load("table/savedQ2.txt")
# agent1 = RLAgent(Qtable1, 1)
# agent2 = RLAgent(Qtable2, 2)

Qt = Qtable()
Qt.load('table/final.txt')

agent = RLAgent(Qt, 2)

agentMin = MinMax(0, 2)
agentMax = MinMax(1, 2)

def signalHandler(sig, frame):
    print("Saving states before exiting....")
    # Qtable1.save("table/savedQ1.txt")
    # Qtable2.save("table/savedQ2.txt")
    Qt.save('table/final.txt')
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler)
signal.signal(signal.SIGILL, signalHandler)

# Change both player inputs to Agents
def getPlayer1Input() -> int:
    # return int(input("Enter move (1): "))
    # return agent1.play(gameBoard)
    return agentMax.play(gameBoard)
    # return agentMin.play(gameBoard)

def getPlayer2Input() -> int:
    # return int(input("Enter move (2): "))
    # return agent1.play(gameBoard)
    # return agentMin.play(gameBoard)
    return agent.play(gameBoard)
    # return agentMax.play(gameBoard)

def winnerMessage(winner):
    print(f"{winner} won!")

def playGame():
    gameBoard.display()
    while True:
        player1move = getPlayer1Input()
        if gameBoard.placeTile(1, player1move) == [-1, -1]:
            sys.exit(1)
        if gameBoard.isWinner(1):
            winnerMessage("red")
            break
        if gameBoard.full():
            winnerMessage("Tie")
            break
        gameBoard.display()
    
        player2move = getPlayer2Input()
        if gameBoard.placeTile(2, player2move) == [-1, -1]:
            sys.exit(1)
        if gameBoard.isWinner(2):
            winnerMessage("yellow")
            break
        if gameBoard.full():
            winnerMessage("Tie")
            break
        gameBoard.display()

    gameBoard.display()
    gameBoard.clear()

if __name__ == "__main__":
    for iteration in range(1000000):
        print(f"----------{iteration}----------")
        playGame()
    # Qtable1.save("table/savedQ1.txt")
    # Qtable2.save("table/savedQ2.txt")
    Qt.save('table/final.txt')
