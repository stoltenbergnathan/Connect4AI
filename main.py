import sys
import signal
from qtable import Qtable
from board import Board
from rlagent import RLAgent
from state import State

gameBoard = Board(None)
Qtable1 = Qtable()
Qtable2 = Qtable()
#Qtable1.load("savedQ1.txt")
#Qtable2.load("savedQ2.txt")
agent1 = RLAgent(Qtable1, 1)
agent2 = RLAgent(Qtable2, 2)

def signalHandler(sig, frame):
    print("Saving states before exiting....")
    Qtable1.save("savedQ1.txt")
    Qtable2.save("savedQ2.txt")
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler)
signal.signal(signal.SIGILL, signalHandler)

# Change both player inputs to Agents
def getPlayer1Input() -> int:
    #return int(input("Enter move (1): "))
    return agent1.play(gameBoard)

def getPlayer2Input() -> int:
    # return int(input("Enter move (2): "))
    return agent2.play(gameBoard)

def winnerMessage(winner):
    print(f"{winner} won!")

def playGame():
    while True:
        player1move = getPlayer1Input()
        if gameBoard.placeTile(1, player1move) == [-1, -1]:
            Qtable1.save("savedQ1.txt")
            Qtable2.save("savedQ2.txt")
            sys.exit(1)
        if gameBoard.isWinner(1):
            winnerMessage("red")
            break
        if gameBoard.full():
            winnerMessage("Tie")
            break
        #gameBoard.display()
    
        player2move = getPlayer2Input()
        if gameBoard.placeTile(2, player2move) == [-1, -1]:
            Qtable1.save("savedQ1.txt")
            Qtable2.save("savedQ2.txt")
            sys.exit(1)
        if gameBoard.isWinner(2):
            winnerMessage("yellow")
            break
        if gameBoard.full():
            winnerMessage("Tie")
            break
        #gameBoard.display()

    gameBoard.display()
    gameBoard.clear()

if __name__ == "__main__":
    for iteration in range(1000000):
        print(f"----------{iteration}----------")
        playGame()
    Qtable1.save("savedQ1.txt")
    Qtable2.save("savedQ2.txt")
